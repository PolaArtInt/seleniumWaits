import time

import pytest
from selenium.webdriver.support import expected_conditions as ec
from locators import URLS, URL2Locks


@pytest.mark.positive
def test_find_elem_with_random_id(driver, exp_wait):
    driver.get(URLS.url_2)

    no_matter_what_id = driver.find_element(*URL2Locks.random_id_text).text
    assert no_matter_what_id == 'This text has random Id', 'Wrong element'


@pytest.mark.positive
def test_enable_after_5_sec_btn(driver, exp_wait):
    driver.get(URLS.url_2)

    btn_evalable = exp_wait.until(ec.element_to_be_clickable(URL2Locks.enable_after_5_sec_btn))
    assert exp_wait.until(
        ec.text_to_be_present_in_element(URL2Locks.enable_after_5_sec_btn, 'Will enable 5 seconds')
    ), 'Wrong text'
    assert btn_evalable.is_enabled(), 'Button is not clickable'


@pytest.mark.positive
def test_color_change_btn(driver, exp_wait):
    driver.get(URLS.url_2)

    color_btn = exp_wait.until(ec.presence_of_element_located(URL2Locks.change_color_btn))

    btn_text_color_before = color_btn.value_of_css_property('color')
    assert btn_text_color_before == 'rgba(255, 255, 255, 1)', 'Button text is not white'

    time.sleep(5)  # button color changes after 5 seconds

    btn_text_color_after = color_btn.value_of_css_property('color')
    assert btn_text_color_after == 'rgba(220, 53, 69, 1)', 'Button text is not red'


@pytest.mark.positive
def test_visible_after_5_sec_btn(driver, exp_wait):
    driver.get(URLS.url_2)

    btn_visible = exp_wait.until(ec.visibility_of_element_located(URL2Locks.visible_after_5_sec_btn))
    assert btn_visible.is_displayed(), 'Button is not visible'

