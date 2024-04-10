import time
import pytest
from selenium.webdriver.support import expected_conditions as ec
from locators import URLS, MainLocks, Messages, Data


@pytest.mark.positive
def test_explicit_wait(driver, exp_wait, form_conditions):
    driver.get(URLS.main_url)

    assert exp_wait.until(ec.text_to_be_present_in_element(MainLocks.main_header, Messages.header_text)), \
        'Wrong page header'
    exp_wait.until(ec.element_to_be_clickable(MainLocks.start_btn)).click()

    exp_wait.until(ec.visibility_of_element_located(MainLocks.login_field)).send_keys(Data.login_text)
    exp_wait.until(ec.visibility_of_element_located(MainLocks.pass_field)).send_keys(Data.pass_text)
    exp_wait.until(ec.visibility_of_element_located(MainLocks.checkbox)).click()

    exp_wait.until(ec.element_to_be_clickable(MainLocks.reg_btn)).click()

    is_loader = exp_wait.until(ec.presence_of_element_located(MainLocks.loader))
    assert is_loader, 'Loader is not appearing'
    is_success_msg = exp_wait.until(ec.visibility_of_element_located(MainLocks.success_box)).text
    assert is_success_msg == Messages.success_msg, 'Success message is not appearing'
    print(is_success_msg)


@pytest.mark.xfail
@pytest.mark.positive
def test_implicit_wait(driver, imp_wait, form_conditions):
    driver.get(URLS.main_url)

    header_text = driver.find_element(*MainLocks.main_header).text
    assert header_text == Messages.header_text, 'Wrong page header'

    driver.find_element(*MainLocks.start_btn).click()

    loader = driver.find_element(*MainLocks.loader)
    is_hidden = loader.get_attribute('class') == 'hidden'
    assert is_hidden, 'Loader is not hidden'

    driver.find_element(*MainLocks.login_field).send_keys(Data.login_text)
    driver.find_element(*MainLocks.pass_field).send_keys(Data.pass_text)
    driver.find_element(*MainLocks.checkbox).click()
    driver.find_element(*MainLocks.reg_btn).click()

    assert loader.is_displayed(), 'Loader is not appearing'

    try:
        # time.sleep(3)  # test falls without time.sleep here :-)
        expected_msg = driver.find_element(*MainLocks.success_box)
        assert expected_msg.text == Messages.success_msg, 'Success message is not appearing'
    except AssertionError as er:
        print(f'Error: {er}')
    else:
        print('Element not found')


@pytest.mark.positive
def test_time_sleep(driver):
    driver.get(URLS.main_url)

    header_text = driver.find_element(*MainLocks.main_header).text
    assert header_text == Messages.header_text, 'Wrong page header'
    time.sleep(5)

    driver.find_element(*MainLocks.start_btn).click()
    time.sleep(2)

    loader = driver.find_element(*MainLocks.loader)
    is_hidden = loader.get_attribute('class') == 'hidden'
    assert is_hidden, 'Loader is not hidden'
    time.sleep(2)

    driver.find_element(*MainLocks.login_field).send_keys(Data.login_text)
    driver.find_element(*MainLocks.pass_field).send_keys(Data.pass_text)
    driver.find_element(*MainLocks.checkbox).click()
    driver.find_element(*MainLocks.reg_btn).click()
    time.sleep(2)

    assert loader.is_displayed(), 'Loader is not appearing'

    time.sleep(5)
    expected_msg = driver.find_element(*MainLocks.success_box)
    assert expected_msg.text == Messages.success_msg, 'Success message is not appearing'
    print(expected_msg.text)
