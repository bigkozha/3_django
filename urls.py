from django.urls import path
from game import views

urlpatterns = [
    path('', views.game),
    path('new_game', views.new_game)
]
