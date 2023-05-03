from django.shortcuts import render, redirect
from Streaming.video_cv2 import *
from Streaming.video_pi import *
from django.http.response import StreamingHttpResponse
from django.views.decorators import gzip
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'live.html', context)
    else:
        return redirect('/accounts/login/')

@gzip.gzip_page
def live(request): 
    if request.user.is_authenticated: 
        try:
            return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
        except HttpResponseServerError as e:
            print("aborted :: "+e)


@gzip.gzip_page
def live_pi(request): 
    """
    try:
        return StreamingHttpResponse(get_picam(PiCameraStreaming()),content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print("aborted :: "+e)
    """
    pass