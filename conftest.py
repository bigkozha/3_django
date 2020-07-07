import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from game.models import Game, Guess

@pytest.yield_fixture(scope="session")
def driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        with webdriver.Chrome(chrome_options=chrome_options) as driver:
            yield driver
    else:
        with webdriver.Remote(command_executor='http://127.0.0.1:9515') as driver:
            yield driver


@pytest.fixture()
def default_games():
    game1 = create_game(1, 100500)
    game2 = create_game(2, 100)
    game3 = create_game(3, 5000)
    games = [game1, game2, game3]

    return games

@pytest.fixture()
def default_guesses():
    guess1 = create_guess(1, 200000)
    guess2 = create_guess(1, 300000)
    guess3 = create_guess(1, 400000)
    guessses = [guess1, guess2, guess3]

    return guessses

def create_game(id, number):
    instance, created = Game.objects.get_or_create(id=id, number=number)
    instance.is_active = True
    instance.save()

    return instance


def create_guess(game_id, number):
    instance, created = Guess.objects.get_or_create(game_id=game_id, number=number)
    instance.save()

    return instance