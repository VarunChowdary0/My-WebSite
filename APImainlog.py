from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
from pymongo import MongoClient
app=Flask("MyAPI")
CORS(app)
@app.route('/')
def loginORsignin():
    return render_template("choose.html")
@app.route('/signup')
def signup():
    return render_template("signup.html")
DataFormat={}
@app.route('/userDataProcess',methods=['POST','GET'])
def process():
    fname=request.form["firstname"]
    lname=request.form["lastname"]
    phno=request.form["phoneNumber"]
    mail=request.form["email"]
    dob=request.form["dob"]
    prof=request.form["Profession"]
    DataFormat["FirstName"]=fname
    DataFormat["LastName"]=lname
    DataFormat["PhoneNumber"]=phno
    DataFormat["Email"]=mail
    DataFormat["DOB"]=dob
    DataFormat["Profession"]=prof
    print(DataFormat)
    return render_template('signIN.html')
@app.route('/signin')
def signin():
    return render_template("signIN.html")
@app.route('/home')
def home():
    return render_template("home.html")
if __name__=='__main__':
    app.run(debug=True,port=2000)