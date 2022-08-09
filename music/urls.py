from django.urls import path 
from . import views 

urls = [
    path('music/', views.MusicList.as_view()),
    path('music/<int:pk>/', views.MusicDetail.as_view())
]