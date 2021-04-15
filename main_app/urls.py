from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_details, name='details'),
    path('games/create/', views.GamesCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GamesUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GamesDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/comments/', views.comments_create, name='comments_create'),
    # path('comments/<int:pk>/update/', views.CommentsUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete/', views.CommentsDelete.as_view(), name='comments_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]