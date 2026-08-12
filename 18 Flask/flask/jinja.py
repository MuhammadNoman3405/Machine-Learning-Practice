from flask import Flask,render_template,request,redirect,url_for

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
# form.html
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

# Variable Rule
# result.html
@app.route('/success/<int:score>')
def success(score):
    return f"You got the marks:{score}"

@app.route('/success/<int:score>')
def success_rel(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template('result.html',results=res)

# another example viva dict expression
# table_result.html
@app.route('/successresult/<int:score>')
def success_res(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    exp={score:res}
    return render_template('table_result.html',results=exp)

# if_condition.html example

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('if_condition.html',results=score)


# Code for getresult.html

@app.route('/submission',methods=['POST','GET'])
def submited():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science + maths + c + data_science)/4
    
    else:
        return render_template('getresult.html')
    return redirect(url_for('success_res',score=int(total_score)))

# now code for Record.html form file
@app.route('/openpage',methods=['POST','GET'])

def form_submission():
    if request.method=='POST':
        student_name=request.form['student_name']
        marks=float(request.form['marks'])
        subject=request.form['subject']
        gender=request.form.get('gender','Not Specified')
        return f"Hello {student_name}! Marks: {marks}, Subject: {subject}, Gender: {gender}"
    
    return render_template('Record.html')
    
        
if __name__=="__main__":
    app.run(debug=True) 