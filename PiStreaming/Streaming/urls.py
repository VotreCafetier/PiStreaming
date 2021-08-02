from django.urls import path
from . import views

urlpatterns = [
    path('live_video/', views.live, name='live'),
    path('', views.index, name='index'),
]
