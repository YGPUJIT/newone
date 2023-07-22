var form=document.getElementById('complaint-body-inner')

form.onsubmit=(e)=>{
    var btn=document.getElementById('complaint-btn')
    btn.disabled=true;
}