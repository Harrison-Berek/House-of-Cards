from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_details, name='details'),
    path('games/create/', views.GamesCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GamesUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GamesDelete.as_view(), name='games_delete'),
    # path('favorites/', views.favorites_index, name='favorites')
]