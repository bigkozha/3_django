from django.shortcuts import render
from game.models import Game, Guess

def game(request):
    games_set = Game.objects.all()
    games = [game for game in games_set]
    return render(request, 'game.html', {'games' : games })