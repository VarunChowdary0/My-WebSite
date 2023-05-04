from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
from pymongo import MongoClient
class connectToDB:
    def connect():
        client=MongoClient('mongodb://localhost:27017')
        db=client['teamXdataBase']
        collection=db['userData']
        return collection
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
    usrnme=request.form['USERNAME']
    pswd=request.form['PASSWORD']
    DataFormat["FirstName"]=fname
    DataFormat["LastName"]=lname
    DataFormat["PhoneNumber"]=phno
    DataFormat["Email"]=mail
    DataFormat["DOB"]=dob
    DataFormat["Profession"]=prof
    DataFormat["username"]=usrnme
    DataFormat['password']=pswd
    collection=connectToDB.connect()
    collection.insert_one(DataFormat)
    print(DataFormat)
    return render_template('signIN.html',flash="",apilink='http://127.0.0.1:2000/verify')
@app.route('/signin')
def signin():
    return render_template("signIN.html",flash="",apilink='http://127.0.0.1:2000/verify')
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/verify',methods=['POST','GET'])
def verification():
    collection=connectToDB.connect()
    chkUsrNme=request.form["usrnme"]
    chkPswd=request.form["pswd"]
    if chkUsrNme is None or chkPswd is None:
        print("not found")
    else:
        verfyDict={}
        verfyDict["username"]=chkUsrNme
        verfyDict["password"]=chkPswd
        for i in collection.find(verfyDict):
            if i is None:
                return 'Invalied'
            else:
                userDataReq=i   
            print(userDataReq)
            if userDataReq["password"]==verfyDict["password"]:
                return render_template("home.html")
            else:
                return 'Wrong pW'
        return render_template("signIN.html",flash="INVALIED CREDENTIALS")
if __name__=='__main__':
    app.run(debug=True,port=2000)