var form=document.getElementById('form')
var button=document.getElementById('login-submit')
form.addEventListener('submit',sendData)


function sendData(e){
    button.disabled=true;
    var f=document.getElementById('form')
    var data=new FormData(form)
    var http=new XMLHttpRequest()
    http.onreadystatechange=function(){
        if(http.status==200 && http.readyState==4){
            var bool=this.responseText
            if(bool.toUpperCase()=='True'.toUpperCase()){
                f.submit()
            }else{
                var warning=document.getElementById('text')
                warning.style.textAlign='center'
                warning.innerHTML='Please check your details'
                button.disabled=false;
            }
        }
    }
    http.open('post','home/loginvalidate',true)
    http.send(data)
    e.preventDefault()
}