def test_index(live_server, driver, default_games, user_client):
    driver.get(live_server.url)

    username = driver.find_element_by_css_selector('[data-test="username"]')
    username.send_keys("user")
    password = driver.find_element_by_css_selector('[data-test="password"]')
    password.send_keys("pass")
    submit = driver.find_element_by_css_selector('[data-test="submit"]')
    submit.click()

    games = driver.find_elements_by_css_selector('[data-test="game"]')
    start_new_game_link = driver.find_element_by_css_selector(
        '[data-test="game-new"]')

    assert len(games) == len(default_games)
    assert start_new_game_link.text == 'Start a new game'


def test_new_game(live_server, driver):
    driver.get(live_server.url + '/new_game')

    element_form = driver.find_element_by_css_selector('[data-test="form"]')
    field_from = element_form.find_element_by_css_selector(
        '[data-test="from"]')
    field_to = element_form.find_element_by_css_selector('[data-test="to"]')
    button_new_game = element_form.find_element_by_css_selector(
        '[data-test="submit"]')

    field_from.send_keys(1)
    field_to.send_keys(2)

    assert field_from.get_attribute("value") == '1'
    assert field_to.get_attribute("value") == '2'

    button_new_game.click()
    assert 'game_detail' in driver.current_url


def test_new_game_string_value_fail(live_server, driver):
    driver.get(live_server.url + '/new_game')

    field_from = driver.find_element_by_css_selector('[data-test="from"]')
    field_to = driver.find_element_by_css_selector('[data-test="to"]')
    button_new_game = driver.find_element_by_css_selector(
        '[data-test="submit"]')

    field_from.send_keys('600000')
    field_to.send_keys(2)
    button_new_game.click()

    assert 'error' in driver.current_url


def test_game_detail(live_server, driver, default_games, default_guesses):
    driver.get(live_server.url + '/game_detail/1')

    guess_form = driver.find_element_by_css_selector(
        '[data-test="guess_form"]')
    guess_items = driver.find_elements_by_css_selector(
        '[data-test="guess_item"]')
    guess_number = driver.find_element_by_css_selector(
        '[data-test="guess_number"]')
    button_make_guess = driver.find_element_by_css_selector(
        '[data-test="submit"]')

    guess_number.send_keys(1)

    assert guess_form is not None
    assert len(default_guesses) == len(guess_items)

    button_make_guess.click()
    assert 'game_detail' in driver.current_url


def test_game_detail_win(live_server, driver, default_games, default_guesses):
    driver.get(live_server.url + '/game_detail/1')

    guess_form = driver.find_element_by_css_selector(
        '[data-test="guess_form"]')
    guess_items = driver.find_elements_by_css_selector(
        '[data-test="guess_item"]')
    guess_number = driver.find_element_by_css_selector(
        '[data-test="guess_number"]')
    button_make_guess = driver.find_element_by_css_selector(
        '[data-test="submit"]')

    guess_number.send_keys(100500)

    assert guess_form is not None
    assert len(default_guesses) == len(guess_items)

    button_make_guess.click()
    assert 'game_detail' in driver.current_url

    is_over = driver.find_element_by_css_selector('[data-test="is_over"]')
    assert is_over.text == 'The game is over. You guessed right'


def test_game_detail_redirect_error_string(live_server, driver, default_games, default_guesses):
    driver.get(live_server.url + '/game_detail/1')

    guess_number = driver.find_element_by_css_selector(
        '[data-test="guess_number"]')
    button_make_guess = driver.find_element_by_css_selector(
        '[data-test="submit"]')

    guess_number.send_keys('abc')

    button_make_guess.click()
    assert 'error' in driver.current_url
