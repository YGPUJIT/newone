var form_button_inner=document.getElementById('form_button_inner')
var form=document.getElementById('main-form')


console.log('CHECK',form_button_inner.disabled)


form.addEventListener('submit',(e)=>{
    form_button_inner.disabled=true;
    form_button_inner.style.backgroundColor="lightgray";
})

// form.onsubmit=(e)=>{
//     console.log('CHECK',form_button_inner.disabled)

//     console.log('CHECK',form_button_inner.disabled)
// }