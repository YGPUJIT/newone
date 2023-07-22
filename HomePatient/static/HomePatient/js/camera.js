var btnStart = document.getElementById( "btn-start" );
var btnStop = document.getElementById("close_camera");
var btnCapture = document.getElementById( "btn-capture" );
var form=document.getElementById('form')

// The stream & capture
var stream = document.getElementById( "stream" );
var capture = document.getElementById( "capture" );
var snapshot = document.getElementById( "snapshot" );

// The video stream
var cameraStream = null;

// Attach listeners
btnStart.addEventListener( "click", startStreaming );
btnStop.addEventListener( "click", stopStreaming );
btnCapture.addEventListener( "click", captureSnapshot );
form.addEventListener('submit',sendData)

// Start Streaming
function startStreaming() {

  var mediaSupport = 'mediaDevices' in navigator;

  if( mediaSupport && null == cameraStream ) {

    navigator.mediaDevices.getUserMedia( { video: true } )
    .then( function( mediaStream ) {

      cameraStream = mediaStream;

      stream.srcObject = mediaStream;

      stream.play();
    })
    .catch( function( err ) {

      console.log( "Unable to access camera: " + err );
    });
  }
  else {

    alert( 'Your browser does not support media devices.' );

    return;
  }
}

// Stop Streaming
function stopStreaming() {

  if( null != cameraStream ) {

    var track = cameraStream.getTracks()[ 0 ];

    track.stop();
    stream.load();

    cameraStream = null;
  }
}



var image_data=[]

function captureSnapshot() {
  if( null != cameraStream ) {
      if(image_data.length<7){
        var ctx = capture.getContext( '2d' );
        var img = new Image();
    
        ctx.drawImage( stream, 0, 0, capture.width, capture.height );
      
        img.src   = capture.toDataURL( "image/png" );
        image_data.push(img.src)
        snapshot.innerHTML="Image "+image_data.length+ " Updated"
      }
  }
}

// var form=document.getElementById('form')
// var data	= new FormData(form);

// function appendImage(imageData,len){
//   form.append("image"+len,imageData,"myimage")
// }



function dataURItoBlob( dataURI ) {

	var byteString = atob( dataURI.split( ',' )[ 1 ] );
	var mimeString = dataURI.split( ',' )[ 0 ].split( ':' )[ 1 ].split( ';' )[ 0 ];
	
	var buffer	= new ArrayBuffer( byteString.length );
	var data	= new DataView( buffer );
	
	for( var i = 0; i < byteString.length; i++ ) {
	
		data.setUint8( i, byteString.charCodeAt( i ) );
	}
	
	return new Blob( [ buffer ], { type: mimeString } );
}

var cam_opt=document.getElementById('camera_opt')
btn=document.getElementById('send')
function sendData(e){
    btn.innerHTML='PLEASE WAIT...'
    btn.disabled=true
    var request = new XMLHttpRequest();
    var form=document.getElementById('form')
    if(cam_opt.checked==true){
      var data	= new FormData();
      for(var i=0;i<image_data.length;i++){
        var dataURI=image_data[i]
        var imageData  = dataURItoBlob(dataURI);
        // data.append("image", imageData,"image"+(i)+".png");
        data.append("image", imageData,"image"+(i)+".png");
      }
      request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          form.submit()
        }
      };
      request.open( "POST", "/home/storeImage", true );
      request.send(data);
    }else{
      e.submit()
    }
    e.preventDefault()
}




