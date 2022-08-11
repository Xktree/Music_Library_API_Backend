from django.urls import path 
from . import views 

urls = [
    path('song/', views.SongList.as_view()),
    path('song/<int:pk>/', views.SongDetail.as_view())
]