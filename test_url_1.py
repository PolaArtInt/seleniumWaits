import pytest
from selenium.webdriver.support import expected_conditions as ec
from locators import URLS, URL1Locks


@pytest.mark.positive
def test_add_box(driver, exp_wait):
    driver.get(URLS.url_1)

    exp_wait.until(ec.element_to_be_clickable(URL1Locks.add_box_btn)).click()
    red_square = exp_wait.until(ec.visibility_of_element_located(URL1Locks.red_box))
    assert red_square.is_displayed(), 'Red square in not appearing'


@pytest.mark.positive
def test_add_box_5_times(driver, exp_wait):
    driver.get(URLS.url_1)

    red_squares = []
    for _ in range(5):
        exp_wait.until(ec.element_to_be_clickable(URL1Locks.add_box_btn)).click()
        red_square = exp_wait.until(ec.visibility_of_element_located(URL1Locks.red_box))
        assert red_square.is_displayed(), 'Red square in not appearing'

        red_squares.append(red_square)

    assert len(red_squares) == 5, 'Wrong length'


@pytest.mark.positive
def test_reveal_input(driver, exp_wait):
    driver.get(URLS.url_1)

    exp_wait.until(ec.element_to_be_clickable(URL1Locks.add_input_btn)).click()
    input_revealed = exp_wait.until(ec.visibility_of_element_located(URL1Locks.new_input))
    assert input_revealed, 'New input in not appearing'


