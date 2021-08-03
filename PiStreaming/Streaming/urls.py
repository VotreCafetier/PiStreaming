from django.urls import path
from . import views

urlpatterns = [
    path('live_videocv2/', views.live, name='live'),
    path('live_videoPi/', views.live_pi, name='live_pi'),
    path('', views.index, name='index'),
]
