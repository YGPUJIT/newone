var action_trigger=document.getElementsByClassName('action-trigger')
var textarea_action=document.getElementById('textarea-action')
textarea_action.addEventListener('blur',reverseAction)

console.log('WORKING')
for(var i=0;i<action_trigger.length;i++){
    action_trigger[i].addEventListener('click',triggerAction)
}



function triggerAction(e){
    textarea_action.setAttribute('placeholder','Escalate the issue to higher officials')
    textarea_action.focus()
}


function reverseAction(){
    textarea_action.removeAttribute('placeholder')
}