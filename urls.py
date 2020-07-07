from django.urls import path
from game import views
from django.urls import path

urlpatterns = [
    path('', views.game),
    path('new_game', views.new_game),
    path('game_detail/<int:game_id>', views.game_detail, name='game_detail'),
    path('error', views.error)
]