import pytest


def test_index(live_server, driver, default_games):
    driver.get(live_server.url)
    games = driver.find_elements_by_css_selector('[data-test="game"]')
    start_new_game_link = driver.find_element_by_css_selector(
        '[data-test="game-new"]')

    assert len(games) == len(games)
    assert start_new_game_link.text == 'Start a new game'


def test_new_game(live_server, driver):
    driver.get(live_server.url + '/new_game')
    element_form = driver.find_element_by_css_selector('[data-test="form"]')
    field_from = element_form.find_element_by_css_selector('#from')
    field_to = element_form.find_element_by_css_selector('#to')
    button_new_game = element_form.find_element_by_css_selector('#submit')
    
    assert element_form is not None
    assert field_to is not None
    assert button_new_game is not None
