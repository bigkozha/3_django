from django.contrib import admin
from django.urls import path

from accounts import views as acviews
from game import views

urlpatterns = [
    path('', views.game),
    path('new_game', views.new_game),
    path('game_detail/<int:game_id>', views.game_detail, name='game_detail'),
    path('error/<text>', views.error, name='error'),
    path('admin/', admin.site.urls),
    path('accounts/login/', acviews.login_view)
]
