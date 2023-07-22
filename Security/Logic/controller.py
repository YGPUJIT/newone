from . import camera
from django.http import StreamingHttpResponse
from django.shortcuts import HttpResponse

cam=camera.Camera()

def StreamingHttp(request,data):
        return StreamingHttpResponse(cam.capture(data),content_type="multipart/x-mixed-replace; boundary=frame")
    

def toggle(request):
        if(cam.checkBoolean()):
                cam.stop()
        else:
                cam.start()
        return HttpResponse('')


def stop(request):
        if((cam.checkBoolean())):
                cam.stop()


def return_offernder():
        return cam.details_offender()


def delete_offender(pid):
        cam.delete_details(pid)