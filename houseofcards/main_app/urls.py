from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='index'),
    path('games/create/', views.GamesCreate.as_view(), name='games_create'),
    path('games/<int:game_id>/', views.games_details, name='details')
    # path('favorites/', views.favorites_index, name='favorites')
]