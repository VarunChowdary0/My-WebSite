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

function verifyUser(){
    const username=document.querySelector(".newUsereName").value;
    const password=document.querySelector(".newPassword").value;
    console.log(`${window.origin}/verify`)
    const objVarify={
        username:username,
        password:password
    }
    fetch(`${window.origin}/verify`,{
        method:['POST','GET'],
        headers:{
            'content-type':'application/JSON'
        },
        body:JSON.stringify(objVarify)
    })
   .then(response=>{
    if(response.ok){
        window.location.href="home";
    }
    else{
        window.location.href="home";
    }
   })
   .catch(error=>{
    console.log("fetch error",error)
   }) 
}
