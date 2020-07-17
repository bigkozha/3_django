from random import randrange

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from game.models import Game, Guess


@login_required
def game(request):
    games = Game.objects.all()
    return render(request, 'game.html', {'games': games})


@login_required
def new_game(request):
    if request.method == 'POST':
        try:
            from_value = int(request.POST['from'])
            to_value = int(request.POST['to'])
            number = randrange(from_value, to_value)
            instance = create_game(number, from_value, to_value)
        except:
            return redirect(reverse('error', args=['guess numbers range was invalid']), request)

        return redirect(reverse('game_detail', args=[instance.id]), request)

    return render(request, 'new_game.html')


@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    guesses = game.guesses.all()

    if request.method == 'POST':
        try:
            guess_value = int(request.POST['guess_number'])
            create_guess(game.id, guess_value, request.user)
        except ValueError:
            return redirect(reverse('error', args=['it is not ur turn']), request)
        except:
            return redirect(reverse('error', args=['guess number was invalid']), request)

        if game.is_active and game.number == guess_value:
            game.is_active = False
            game.save()

    return render(request, 'game_detail.html', {'game': game, 'guesses': guesses})


def create_game(number, from_value, to_value):
    if not is_valid_number(number):
        raise Exception('number is not valid')
    try:
        instance = Game.objects.create(
            number=number, is_active=True, from_number=from_value, to_number=to_value)
        return instance
    except:
        print('an error occured: create_game')


def create_guess(game_id, number, user):
    if not is_valid_number(number):
        raise Exception('number is not valid')
    if not is_correct_guesser(game_id, user):
        raise ValueError('user is not correct for turn')
    try:
        instance = Guess.objects.create(game_id=game_id, number=number, user=user)
        return instance
    except:
        print('an error occured: create_guess')


def is_valid_number(number):
    if number is None:
        return False
    return True


def is_correct_guesser(game_id, user):
    guesses = list(Guess.objects.filter(game_id=game_id))
    if len(guesses) > 0:
        if guesses[-1].user is not None:
            if guesses[-1].user.id == user.id:
                return False
    return True


def error(request, text):
    return render(request, 'error.html', {'text': text})
