


function possibleOffender(id,name,time){
    var fields=[id,name,time];
    var app=["ID: ",'Name: ','Time: ']
    var div=document.createElement('div');
    var btn=document.createElement('button')
    var btn2=document.createElement('button')
    btn2.innerHTML='Search'
    btn.innerHTML="Remove"
    for(var i=0;i<fields.length;i++){
        var p=document.createElement('p');
        var val=app[i] +fields[i]
        var text=document.createTextNode(val);
        p.appendChild(text);
        div.appendChild(p);
    }
    btn.setAttribute('class','action')
    btn.setAttribute('value',id)
    btn2.setAttribute('value',id)
    btn2.setAttribute('class','search')
    btn.addEventListener('click',takeAction)
    btn2.addEventListener('click',searchButton)
    div.appendChild(btn2)
    div.appendChild(btn)
    return div;
}


// function searchButton(){
//     console.log("INININININI")
// }




var btn=document.getElementById('action')
var data=document.getElementById('possible-offenders')
function createElement(){
    var http=new XMLHttpRequest()
    http.onreadystatechange=function(){
        var pid=checkID()
        if(this.readyState==4 && this.status==200){
            // data.innerHTML="<h3>Possbile offender</h3>";
            var RT=this.responseText
            offenders=JSON.parse(RT)
            for(val in offenders){
                if(!pid.includes(val)){
                    var doctorIntiation=offenders[val][2]
                    var name=offenders[val][1]
                    var time=offenders[val][0]
                    var ele=possibleOffender(val,name,time)
                    ele.classList.add('person-info')
                    data.appendChild(ele)
                }
            }
            data.scrollTop = data.scrollHeight
        }
    }
    http.open('POST','/Security/offender',true)
    http.send()
}

// var ele=setInterval(createElement,30000)
var refresh=document.getElementById('refresh')
refresh.addEventListener('click',createElement)

function takeAction(e){
    console.log("INININI")
    var http=new XMLHttpRequest()
    var value=this.value
    var ele=this
    ele.innerHTML="Removed"
    ele.disabled=true
    http.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            parent=ele.parentNode
            ele.parentNode.parentNode.removeChild(parent)
        }
    }
    http.open('GET','/Security/removeOffender?id='+value,true)
    http.send()
}


function checkID(){
    var person_info=document.getElementsByClassName('person-info')
    var id=[]
    for(var i=0;i<person_info.length;i++){
        var btnValue=person_info[i].getElementsByClassName('action')[0].value
        id.push(btnValue)
    }
    return id
}