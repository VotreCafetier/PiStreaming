from django.shortcuts import render
from Streaming.video_cv2 import *
from Streaming.video_pi import *
from django.http.response import StreamingHttpResponse
from django.views.decorators import gzip

# Create your views here.
def index(request):
    context = {}
    return render(request, 'live.html', context)

@gzip.gzip_page
def live(request): 
    try:
        return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted :: "+e)


@gzip.gzip_page
def live_pi(request): 
    try:
        return StreamingHttpResponse(get_picam(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted :: "+e)