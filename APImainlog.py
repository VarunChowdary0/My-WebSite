from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
from bson import ObjectId
import json
from urllib.parse import quote_plus
from pymongo.server_api import ServerApi
class connectToDB:
    def connect():
        client = MongoClient("mongodb+srv://user_Application:application@cluster0.epypnho.mongodb.net/?retryWrites=true&w=majority")
        db = client['teamXdataBase']
        db=client['teamXdataBase']
        collection=db['userData']
        return collection
    def chatDB():

        client = MongoClient("mongodb+srv://user_Application:application@cluster0.epypnho.mongodb.net/?retryWrites=true&w=majority")
        db = client['teamXdataBase']
        db=client['teamXdataBase']
        collection=db['chatINFO']
        return collection
userFindDict={}
userInfo={}
signedin=False
class UserData():
    def __init__(self) -> None:
        pass
    def info():
        collection=connectToDB.connect()
        dataInfo=collection.find()
        return dataInfo
    def require(key):
        collection=connectToDB.connect()
        dataMy=(collection.find_one(userFindDict))
        if key =='username':
            return dataMy['username']
        elif key=='FirstName':
            return dataMy['FirstName']
        elif key=='LastName':
            return dataMy['LastName']
        elif key=='PhoneNumber':
            return dataMy['PhoneNumber']
        elif key=='Email':
            return dataMy['Email']
        elif key=='DOB':
            return dataMy['DOB']
        elif key=='Profession':
            return dataMy['Profession']
        elif key=='pampi':
            return dataMy['password']
        elif key=='password':
            return 'Not Found'
        else:
            return False
    def userIndvidulaInfo():
        collection=connectToDB.connect()
        dataMy=(collection.find_one(userFindDict))
        return dataMy

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
    checkDict={}
    checkDict["PhoneNumber"]=phno
    checkDict["Email"]=mail
    checkDict["username"]=usrnme
    check=connectToDB.connect()
    res=check.find(checkDict)
    if(res is None):
        DataFormat["FirstName"]=fname
        DataFormat["LastName"]=lname
        DataFormat["PhoneNumber"]=phno
        DataFormat["Email"]=mail
        DataFormat["DOB"]=dob
        DataFormat["Profession"]=prof
        DataFormat["username"]=usrnme
        DataFormat['password']=pswd
        DataFormat['_id']=ObjectId()
        collection=connectToDB.connect()
        collection.insert_one(DataFormat)
        print("creating")
        #print(DataFormat)
        return render_template('signIN.html',flash="")
    else:
        print("Already exists")
        return render_template("dupicate.html")
@app.route('/signin')
def signin():
    return render_template("signIN.html",flash="")
@app.route('/home')
def home():
    return render_template("home.html",nameOfUser='GUEST')
@app.route('/verify',methods=['POST','GET'])
def verification():
    global userFindDict
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
            #print("info",userInfo)
            #print('DBres',userDataReq)
            if userDataReq["password"]==verfyDict["password"]:
                global signedin
                signedin=True
                userFindDict=verfyDict
                #print(userFindDict)
                #print("userFindDict",userFindDict)
                firstname=UserData.require('FirstName')
                lastname=UserData.require('LastName')
                user=firstname+' '+lastname
                return render_template("home.html",nameOfUser=user)
            else:
                return 'Wrong pW'
        return render_template("signIN.html",flash="INVALIED CREDENTIALS")
@app.route('/accessUserData/<username>/<password>')
def access(username,password):
    if username=='admin_getMe*' and password =='access><varun':
        data = UserData.info()
        user_data = [json.loads(json_util.dumps(doc)) for doc in data]
        #print(user_data)
        return jsonify(user_data)
    else:
        return 'NO ACCESS'
#function to debug
@app.route('/wowow')
def woow():
    #print(UserData.userIndvidulaInfo())
    #print(userFindDict)
    user=UserData.userIndvidulaInfo()
    #print('user_->', user['FirstName']+user['LastName'])
    getit=input("Enter req: ")
    name=UserData.require(getit)
   # print(name)
    return 'Done'

@app.route('/chatZone')
def chatPage():
    return render_template("publicChat.html")
@app.route('/chatAPI',methods=['POST','GET'])
def saveThechat():
    collection=connectToDB.chatDB()
    chatData=request.get_json()
    getUsername=UserData.userIndvidulaInfo()
    chatData['_Id']=ObjectId()
    username=getUsername['username']
    collection.insert_one(chatData)
    #print(chatData)
    response=jsonify()
    response.status_code=200
    return response
@app.route('/GetChatArr',methods=['GET'])
def GetChatArr():
    collection=connectToDB.chatDB()
    chatList=[]
    for chat in collection.find():
        chatList.append(chat)
    #print(chatList)
    return json_util.dumps(chatList)

@app.route('/GetUsername')
def GetUsername():
    name=UserData.require('username')
    return json_util.dumps(name)

@app.route('/logout')
def logger():
    logout()
    return render_template('choose.html')
@app.route('/signinStatus')
def signinStatus():
    return json_util.dumps(signedin)
#function to logout
def logout():
    global userFindDict,userInfo,user
    global signedin
    signedin=False
    user=''
    userFindDict={}
    userInfo={}
    return userFindDict,userInfo
if __name__=='__main__':
    app.run(debug=True,port=2000,host="0.0.0.0")