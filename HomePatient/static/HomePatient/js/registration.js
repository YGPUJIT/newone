var photo=document.getElementsByClassName('part')
console.log(photo)
var left=document.getElementById('left')
left.addEventListener('click',decrement)
var right=document.getElementById('right')
right.addEventListener('click',increment)
var display_page=0
var total_length=photo.length
var camera=document.getElementById('camera-window')
var btn_start=document.getElementById('btn-start')
var body=document.getElementById('body')
var close=document.getElementById('close_camera')
btn_start.addEventListener('click',()=>{
    camera.classList.toggle('none')
    body.classList.toggle('remove_bg')
})
var desk_opt=document.getElementById('desktop_opt')
var cam_opt=document.getElementById('camera_opt')
desk_opt.checked=true
btn_start.disabled=true

desk_opt.addEventListener('change',()=>{
    console.log("desk_event")
    if(desk_opt.checked==true){
        btn_start.disabled=true
        p1.disabled=false
    }
})
p1=document.getElementById('p1')
cam_opt.addEventListener('change',()=>{
    console.log("cam_event")
    if(cam_opt.checked==true){
        p1.disabled=true
        btn_start.disabled=false
    }
})



close.addEventListener('click',()=>{
    camera.classList.toggle('none')
})

// window.onresize=dothis
// window.onload=dothis

function dothis(){
    var body=document.getElementById('main-body')
    body.style.minHeight=screen.height+'px';    
}

function hide(){
    for(var i=0;i<photo.length;i++){
        photo[i].classList.add('display_hidden')
    }    
    photo[0].classList.toggle('display_hidden')
};

hide()

function decrement(){
    photo[display_page].classList.toggle('display_hidden')
    if(display_page==0){
        display_page=total_length-1;
    }else{
        display_page=display_page-1;
    }
    photo[display_page].classList.toggle('display_hidden')
}


function increment(ele){
    photo[display_page].classList.toggle('display_hidden')
    display_page=(display_page+1)%total_length
    photo[display_page].classList.toggle('display_hidden')
}



