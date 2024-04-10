import time
import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from locators import URLS, URL3Locks


@pytest.mark.positive
def test_element_hidden(driver, exp_wait):
    driver.get(URLS.url_3)
    exp_wait.until(ec.presence_of_element_located(URL3Locks.link_1)).click()

    # element already apears in DOM, but hidden:
    hello = exp_wait.until(ec.presence_of_element_located(URL3Locks.final_msg))
    style_before = hello.value_of_css_property('display')
    assert style_before == 'none', 'Element is not hidden'

    header = driver.find_element(*URL3Locks.page_header_h4)
    assert header.text == 'Example 1: Element on page that is hidden', 'Wrong header'

    exp_wait.until(ec.presence_of_element_located(URL3Locks.start_btn)).click()
    loader = driver.find_element(*URL3Locks.loader)
    assert loader.is_displayed(), 'Loader is not displayed'

    time.sleep(5)  # wait until css property changes

    style_after = hello.value_of_css_property('display')
    assert style_after == 'block', 'Element is not visible'
    assert hello.text == 'Hello World!', 'Wrong message'


@pytest.mark.positive
def test_element_rendered_after(driver, exp_wait):
    driver.get(URLS.url_3)
    exp_wait.until(ec.presence_of_element_located(URL3Locks.link_2)).click()

    header = driver.find_element(*URL3Locks.page_header_h4)
    assert header.text == 'Example 2: Element rendered after the fact', 'Wrong header'

    # element in not located in DOM yet:
    try:
        exp_wait.until(ec.presence_of_element_located(URL3Locks.final_msg))
    except (NoSuchElementException, TimeoutException, AssertionError):
        pass

    exp_wait.until(ec.presence_of_element_located(URL3Locks.start_btn)).click()
    loader = driver.find_element(*URL3Locks.loader)
    assert loader.is_displayed(), 'Loader is not displayed'

    # element is rendering just now:
    hello = exp_wait.until(ec.presence_of_element_located(URL3Locks.final_msg))
    style_of_rendered = hello.value_of_css_property('display')
    assert style_of_rendered == 'block', 'Element is hidden'

    assert hello.text == 'Hello World!', 'Wrong message'
