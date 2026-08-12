from flask import Flask

app=Flask(__name__)
@app.route("/")

def welcome():
    return f"Welcome to the flask app. Which will be used to learn the flask"

@app.route("/index")
def index():
    return f"This is the index page"

if __name__=="__main__":
    app.run(debug=True) 