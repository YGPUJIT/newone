var btn_show=document.getElementsByClassName('btn-show')
var btn_hide=document.getElementsByClassName('btn-hide')
var ignore_form=document.getElementsByClassName('ignore-form')
var take_action=document.getElementsByClassName('take-action')


for(var i=0;i<btn_show.length;i++){
    btn_show[i].addEventListener('click',toggle)
    btn_hide[i].addEventListener('click',toggle)
    ignore_form[i].addEventListener('submit',sendRequest)
    take_action[i].addEventListener('submit',sendAction)
}

function toggle(e){
    console.log('ININ')
    var ele=this.parentElement.parentElement
    var display_content=ele.getElementsByClassName('complaint-info-middle-complaint')[0]
    display_content.classList.toggle('display-hide')
    this.classList.toggle('display-hide')
    if(this.classList.value.includes('btn-show')){
            this.parentElement.getElementsByClassName('btn-hide')[0].classList.toggle('display-hide')
    }else{
            this.parentElement.getElementsByClassName('btn-show')[0].classList.toggle('display-hide')
    }
}


function sendRequest(e){
    var btn=this.getElementsByClassName('btn')[0]
    btn.innerHTML='PLEASE WAIT'
    btn.disabled=true
}

function sendAction(e){
    e.preventDefault();
    href=this.action
    console.log(href)
    var xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            res=this.responseText
            if(res!='false'){
                complaint_token=JSON.parse(res)
                var doctorComplaintTokenid=document.getElementById('doctor-complaint-tokenid')
                var doctorComplaintId=document.getElementById('doctor-complaint-id')
                doctorComplaintId.value=complaint_token['did']
                doctorComplaintTokenid.value=complaint_token['token']
            }
        }
    }
    xhttp.open("POST",href,true)
    xhttp.send()
}


