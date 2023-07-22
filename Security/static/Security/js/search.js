var patient_information=document.getElementById('security-main-inner-information')
var searchValue=document.getElementById('patient-search')
var searchBtn=document.getElementById('searchBtn')
// var notification_btn=document.getElementById('alert-official')


searchBtn.addEventListener('click',search)


var patient_id=null


function createRequest(searchVal){
    patient_information.innerHTML=""
    var http=new XMLHttpRequest()
    http.onreadystatechange=function(){
        if(http.readyState==4 && http.status==200){
            var information=http.responseText
            createInformation(JSON.parse(information))
        }
    }
    assignPatientID(searchVal)
    http.open('GET','/Security/getInformation?searchId='+searchVal,true)
    http.send()
}

function search(e){
    var searchVal=searchValue.value
    createRequest(searchVal)
}

function clearInformation(){
    patient_information.innerHTML=""
    var patient_search=document.getElementById('patient-search')
    patient_search.value=""
}


function createInformation(information){
    var div=document.createElement('div')
    div.setAttribute('id','information-inner')
    var clear_btn=document.createElement('button')
    clear_btn.innerHTML='X'
    clear_btn.classList.add('pullright')
    clear_btn.setAttribute('id','clear-btn')
    clear_btn.addEventListener('click',clearInformation)
    div.appendChild(clear_btn)
    for(var key in information){
        if(key=='href'){
            var image_text=document.createElement('p')
            image_text.innerHTML="Please check the images before confrontation"
            div.appendChild(image_text)
            var img=document.createElement('img')
            img.src=information['href']
            div.appendChild(img)
            continue
        }
        var value=information[key]
        var p=document.createElement('p')
        var text=document.createTextNode(key+": "+value)
        p.appendChild(text)
        div.appendChild(p)
    }
    patient_information.appendChild(div)
    var notification_button=createNotificationButton(information)
    patient_information.appendChild(notification_button)
}



function createNotificationButton(information){
    var notification_button=document.createElement('button')
    notification_button.innerHTML="Alert! Hospital"
    notification_button.setAttribute('id','alert-official')
    notification_button.setAttribute('class','alert-official-class')
    notification_button.addEventListener('click',send_notification)
    return notification_button
}


function searchButton(){
    var val=this.value
    searchValue.value=val
    createRequest(val)
}


function send_notification(e){
    var ele=document.getElementById('alert-official')
    ele.disabled=true
    ele.style.backgroundColor='gray'
    ele.innerHTML='ALERTED'
    var http=new XMLHttpRequest()
    http.onreadystatechange=function(){
        console.log('Successful')
    }
    http.open('GET','/Security/sendAlert?searchId='+patient_id)
    http.send()
}


function assignPatientID(id){
    patient_id=id
}