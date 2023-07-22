function loadDoc() {
  console.log('loadDOC in')
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/Security/toggle", true);
    xhttp.send();
  }


window.onbeforeunload=()=>{
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/Security/stop", true);
    xhttp.send();
}