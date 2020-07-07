from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from game.models import Game, Guess
from random import randrange

NUMBER_MAX_VALUE = 500000
NUMBER_MIN_VALUE = 0

def game(request):
    games_set = Game.objects.all()
    games = [game for game in games_set]
    return render(request, 'game.html', {'games': games})


def new_game(request):
    if request.method == 'POST':
        try:
            from_value = int(request.POST['from'])
            to_value = int(request.POST['to'])
            number = randrange(from_value, to_value)
            instance = create_game(number)
        except:
            return redirect('/error', request)

        
        return redirect(reverse('game_detail', args=[instance.id]), request)

    return render(request, 'new_game.html')


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    guesses = game.guesses.all()

    if request.method == 'POST':
        try:
            guess_value = int(request.POST['guess_number'])
            create_guess(game.id, guess_value)
        except:
            return redirect('/error', request)
            
        if game.is_active and game.number == guess_value:
            game.is_active = False
            game.save()

    return render(request, 'game_detail.html', {'game': game, 'guesses': guesses})


def create_game(number):
    if not is_valid_number(number):
        raise Exception('number is not valid')
    try:
        instance = Game.objects.create(number=number, is_active=True)
        return instance
    except:
        print('an error occured: create_game')


def create_guess(game_id, number):
    if not is_valid_number(number):
        raise Exception('number is not valid')
    try:
        instance = Guess.objects.create(game_id=game_id, number=number)
        return instance
    except:
        print('an error occured: create_guess')

def is_valid_number(number):
    if number >= NUMBER_MAX_VALUE or number <= NUMBER_MIN_VALUE:
        return False
    if number is None:
        return False
    return True
        

def error(request):
    return render(request, 'error.html')
