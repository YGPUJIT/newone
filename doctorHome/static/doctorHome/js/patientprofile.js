var addmedicine=document.getElementById('addMedicine')
addmedicine.addEventListener('click',addElement)


function addElement(){
    var medicine_name=document.getElementById("medicine_name").value
    document.getElementById("medicine_name").value=""
    var medicine_directive=document.getElementById("medicine_directive").value
    document.getElementById("medicine_directive").value=""
    if(medicine_name.trim().length==0 || medicine_directive.trim().length==0){
        alert("Please enter both values")
        return
    }
    var container=document.getElementById('medicine-form-tab')
    var div=createInput(medicine_name,medicine_directive)
    container.appendChild(div)
}

function createInput(inputValue,directive){
    var div=document.createElement('div')
    div.classList.add('medicine-form-tab-medicine')
    var input=document.createElement('input')
    var input2=document.createElement('input')
    input.value=inputValue
    input.name='medicine_name'
    input2.value=directive
    input2.name='directive'
    input2.style.display='none'
    input.setAttribute('readonly',true)
    var span=document.createElement('span')
    span.addEventListener('click',deleteParent)
    span.innerHTML='X'
    div.appendChild(input)
    div.appendChild(input2)
    div.appendChild(span)
    return div
}


function deleteParent(){
    var parent=this.parentElement
    parent.remove()
}