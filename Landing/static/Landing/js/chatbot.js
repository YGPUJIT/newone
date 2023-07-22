//chat-bot
var ele=document.getElementById('chat-bot-open-close').addEventListener('click',close_and_open)
var chat_bot_text=document.getElementById('chat-bot-text').addEventListener('keyup',dummy)
var close=true

var check=true


function createTextChat(textRandom,leftOrRight){
    var ele=document.createElement('p')
    var main=document.getElementById('chat-bot-content-inner')
    var textNode=document.createTextNode(textRandom)
    ele.innerHTML=textRandom
    ele.classList.add('chat-box-text')
    ele.classList.add(leftOrRight)
    main.append(ele)
    main.scrollTop=main.scrollHeight
}

function loadDoc(callback,tv) {
    var xhttp = new XMLHttpRequest();
    var f=new FormData();
    xhttp.onreadystatechange = function() {
        if ( this.readyState == 4 &&this.status == 200) {
            console.log("AJAX")
            return callback(this.responseText);
       }
    };
    xhttp.open("POST", "/chatBot",true);
    f.append('q',tv)
    // console.log(f)
    xhttp.send(f);
}

function dummy(e){
    if(e.keyCode==13){
        var text=document.getElementById('chat-bot-text')
        var textValue=text.value
        if(textValue.trim().length==0)
            return
        if(textValue.trim().length!=0){
            createTextChat(textValue,'display-right')
            text.value=''
            loadDoc((ret)=>{
                 createTextChat(ret,'display-left')
            },textValue)
        }
    }
 }

function close_and_open(e){
    var main=document.getElementById('chat-bot-content-inner')
    main.scrollTop=main.scrollHeight
    var full=document.getElementById('chat-bot-inner')
    var container=document.getElementById('chat-bot-content')
    container.classList.toggle('display-full')
    full.classList.toggle('display-three')
    if(close){
        // var main=document.getElementById('chat-bot-content-inner')
        // main.innerHTML="";
        if(check){
            createTextChat('Hi there! How can I help you?','display-left')
            check=false
        }
    }
    close=close?false:true
}

