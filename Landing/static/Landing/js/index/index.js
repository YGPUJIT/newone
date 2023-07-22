
var body=document.getElementById('header')
var h_info=document.getElementsByClassName('header-info-right')[0]

body.onclick=()=>{
    if(h_info.classList.contains('not-hide')){
        drop_and_up()
    }
}

function drop_and_up(){
    h_info.classList.toggle('hide')
    h_info.classList.toggle('not-hide')
}