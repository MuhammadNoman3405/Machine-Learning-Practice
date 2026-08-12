from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")

def welcome():
    return f"<html><H1>Welcome to the flask app. Which will be used to learn the flask</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# get and post method
@app.route('/form',methods=['GET','POST'])

def form():
 if request.method=='POST':
   name= request.form['name']
   return f"Hello {name} how are you?"
 return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])

def submit():
 if request.method=='POST':
   name= request.form['name']
   return f"Hello {name} how are you?"
 return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True) 