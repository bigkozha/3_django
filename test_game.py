import pytest


def test_index(live_server, driver, default_games):
    driver.get(live_server.url)
    games = driver.find_elements_by_css_selector('[data-test="game"]')
    start_new_game_link = driver.find_element_by_css_selector('body > a')
    
    assert len(games) == len(games)
    assert start_new_game_link.text == 'Start a new game'

def test_index_nogames(live_server, driver):
    driver.get(live_server.url)
    element = driver.find_element_by_css_selector('body > a')

    assert element.text == 'Start a new game'


