from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.home, name='home'),
    path('player/<int:pk>/', views.player_detail, name='player_detail'),
    path('matches/', views.matches, name='matches'),
]
