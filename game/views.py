from django.shortcuts import render, get_object_or_404
from django.http import Http404
from game.models import Game, Guess


def game(request):
    games_set = Game.objects.all()
    games = [game for game in games_set]
    return render(request, 'game.html', {'games': games})


def new_game(request):
    return render(request, 'new_game.html')


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    guesses = Guess.objects.filter(game__id=game_id)
    
    return render(request, 'game_detail.html', {'game': game, 'guesses': guesses})
