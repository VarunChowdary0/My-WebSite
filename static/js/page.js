function learn(){
    const change=document.querySelector(".done_it").innerHTML=`               
    <button onclick="FrontEnd()" class="start frontEnd"> learn Front End</button>
    <hr class="hr_button">
    <button onclick="BackEnd()" class="start BackEnd"> learn Back End</button>
    <hr class="second">`;
}
function FrontEnd(){
    const change=document.querySelector(".done_it").innerHTML='';
    const change_1=document.querySelector(".roadmap").innerHTML=`
    <p>ROADMAP TO LEARN</p>
    <p>HTML CSS JAVASCRIPT</p>
    `;
    const changeROadMap=document.querySelector(".roadmap").innerHTML=`
    <a href=""><div onclick="htmlContent()" class="c10 co">HTML</div></a>
    <a href=""><div onclick="cssContent()" class="c10 co">CSS</div></a>
    <a href=""><div onclick="JsContent()" class="c10 co">JavaScript</div></a>
    `;
}
function BackEnd(){
    const change=document.querySelector(".done_it").innerHTML='';
    const change_1=document.querySelector(".roadmap").innerHTML=`
    <p>ROADMAP TO LEARN</p>
    <p>MONGODB JAVASCRIPT FLASK</p>
    `;
    const changeROadMap=document.querySelector(".roadmap").innerHTML=`
    <a href=""><div onclick="JsContent()" class="c10 co">JavaScript</div></a>
    <a href=""><div onclick="FlaskContent()" class="c10 co">Flask</div></a>
    <a href=""><div onclick="MongoContent()" class="c10 co">MongoDB</div></a>
    `;
}
function htmlContent(){
    //const change

}
function readData(){
    let fname=document.querySelector(".fname");
    let lname=document.querySelector(".lname");
    let phon=document.querySelector(".phno");
    let mail=document.querySelector(".mail");
    let dob=document.querySelector(".dob").value;
    let prof=document.querySelector(".selector").value;
    let usrnme=document.querySelector(".newUserName");
    let pswd=document.querySelector(".newPassword");
    if(fname.value.length!=0 && lname.value.length!=0 && phon.value.length!=0 && mail.value.length!=0 && usrnme.length!=0 && pswd.length!=0 && dob!='' && prof!=''){
        let boom=document.querySelector(".sendData")
        boom.style.opacity="0";
        boom.style.height="0px";
        boom.style.width="0px";
    }
}
//---------------------------------save username------------
let username;
function GetUsername(){
    const kaboom=document.querySelector(".newUserName");
    username=kaboom.value;
}


//--------------ChatBox--------------------
const messageInfo={
    MyMessage:'',
    time:'',
    date:''
}
let chatDataArr = [];
/*
function validateData() {
    // show the chat on page
    username="uuuuuu";
   fetch('/GetChatArr')
      .then(response => response.json())
      .then(data => {
        chatDataArr=data;

      })
  }
  */
 window.onload=function pageload(){
    if(window.location.pathname=='/chatZone'){
        document.querySelector(".usersName").innerHTML=username;
        let animate_=document.querySelector(".top_chatpg");
        animate_.style.borderBottomLeftRadius= "100px";
        animate_.style.borderBottomRightRadius= "100px";
        console.log("kaboom !!");
        console.log("n_0:",username)
        giveChat();
    }
 }
 function giveChat(){
    let refr=document.querySelector(".messages");
    refr.innerHTML='';
    globalThis.giveChat = giveChat;
    window.giveChat = giveChat;
    if(window.location.pathname=='/chatZone'){
                                                                /* username=fetch('/GetUsername')
                                                                        .then(response=>response.json())
                                                                        .then(data=>{
                                                                            username=data
                                                                            return data
                                                                        }) */
        fetch('/GetChatArr')
        .then(response => response.json())
        .then(data => {
            chatDataArr=data;
            console.log(chatDataArr)
            console.log("n_:",username)
                    /* main chat code */
            messageBOX=document.querySelector(".messages");
                                                                    //const usersName=document.querySelector(".usersName").innerHTML=`${username}`;
            for(i=0;i<chatDataArr.length;i++)
            {
                if(chatDataArr[i]['username']===username)
                {
                    messageBOX.innerHTML+=`
                    <div class="my_msg">
                    <div class="myName_">${username}</div>
                    <div class="msg_of_mine">${chatDataArr[i]['MyMessage']}</div>
                    <p class="time">${chatDataArr[i]['time']}</p>
                    </div>
                    `;
                    //console.log(`name:${username},message:${chatDataArr[i]['MyMessage']},time:${chatDataArr[i]['time']}`)
                }
                else{
                    messageBOX.innerHTML+=`
                    <div class="others_msg">
                    <div class="nameOfUser_">${chatDataArr[i]['username']}</div>
                    <div class="msg_of_other">${chatDataArr[i]['MyMessage']}</div>
                    <p class="time">${chatDataArr[i]['time']}</p>
                    </div>
                    `;
                }
            }
    
        })
}}

function opp(){
    
    const newMessage=document.querySelector(".newMessage").value;
    if(newMessage.length>=2){
        const date= new Date();
    const strDate=date.toLocaleDateString();
    const strTime=date.toLocaleTimeString();
    messageInfo.MyMessage=newMessage;
    messageInfo.date=strDate;
    messageInfo.time=strTime;
    console.log(messageInfo);

    document.querySelector(".newMessage").value='';
    fetch(`${window.origin}/chatAPI`,{
        method:'POST',
        headers:{
            'Content-type':'application/JSON'
        },
        body:JSON.stringify(messageInfo)
    })
    .then(response=>{
        if(response.ok){
            giveChat();
        }
        else{
            console.log("failed");
        }
    })
    .catch(error=>{
        console.log("fetch error:",error);
    })
    }
                                                                                                } /*
                                                                                                let name_=document.querySelector(".usersName").innerHTML;
                                                                                                function keepMeLogged(){
                                                                                                    while(name_===null){
                                                                                                        setInterval(name_=document.querySelector(".usersName").innerHTML,1000);
                                                                                                    };
                                                                                                }

                                                                                                if(window.location.pathname=='/chatZone'){
                                                                                                    setInterval(GetUsername,1);
                                                                                                }
                                                                                                */