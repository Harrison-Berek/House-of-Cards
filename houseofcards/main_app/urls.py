from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='index'),
    path('games/create/', views.GamesCreate.as_view(), name='games_create'),
    # path('favorites/', views.favorites_index, name='favorites')
]