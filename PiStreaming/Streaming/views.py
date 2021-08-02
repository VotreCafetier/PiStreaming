from django.shortcuts import render
from Streaming.video import *

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def live(request):
    frame = livefeed.update()
    context = {frame}
    return render(request, 'live.html', context)