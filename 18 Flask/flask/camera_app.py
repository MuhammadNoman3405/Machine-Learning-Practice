from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Camera initialization
camera = cv2.VideoCapture(0)

# Load Haar Cascades once (Outside the frame loop for optimal FPS)
# Using cv2.data.haarcascades ensures it never fails even if local path is missing
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def generate_frame():
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # 1. Convert frame to Grayscale first
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 2. Detect Faces on Grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        # 3. Draw Bounding Boxes for Faces and Eyes
        for (x, y, w, h) in faces:
            # Draw Face rectangle (Blue)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Region of Interest (ROI) for face
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            
            # Detect Eyes inside the Face ROI
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3)
            for (ex, ey, ew, eh) in eyes:
                # Draw Eye rectangle (Green)
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # 4. Encode frame as JPEG for streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('opencv.html')

@app.route('/Video')
def Video():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)