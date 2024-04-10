import time
import pytest
import requests
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from locators import URLS, HerokuApp


@pytest.mark.positive
def test_create_and_delete_element(driver, exp_wait):
    driver.get(URLS.heroku_1)

    page_header = exp_wait.until(ec.presence_of_element_located(HerokuApp.header_h3))
    assert page_header.text == 'Add/Remove Elements'

    exp_wait.until(ec.element_to_be_clickable(HerokuApp.add_btn)).click()

    new_btn = exp_wait.until(ec.element_to_be_clickable(HerokuApp.del_btn))
    assert new_btn.is_displayed(), 'New element is not found'

    new_btn.click()

    btn_invisible = exp_wait.until(ec.invisibility_of_element(HerokuApp.del_btn))
    assert btn_invisible, 'New element is not hidden'


@pytest.mark.xfail
@pytest.mark.negative
def test_base_auth_negative_try_alert(driver, exp_wait):
    driver.get(URLS.heroku_2)

    try:
        exp_wait.until(ec.alert_is_present())
        driver.switch_to.alert.accept()
    except (NoAlertPresentException, TimeoutException):
        pass
    else:
        print('No alert is displayed')


@pytest.mark.positive
def test_base_auth_browser_dialog_window(driver):
    driver.get(URLS.heroku_2)

    # to handle browser dialog window, append credentials (username and password) with the url
    # https://username:password@siteurl:
    driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')

    page_header = driver.find_element(*HerokuApp.header)
    page_msg = driver.find_element(*HerokuApp.text)
    assert page_header.text == 'Basic Auth' and \
           page_msg.text == 'Congratulations! You must have the proper credentials.', 'Wrong auth'


@pytest.mark.positive
def test_brocken_imgs(driver):
    driver.get(URLS.heroku_3)

    imgs = driver.find_elements(*HerokuApp.page_imgs)[:-1]
    counter = 0
    res_imgs = []
    resps = []

    for img in imgs:
        img_src = img.get_attribute('src')
        response = requests.get(img.get_attribute('src'), stream=True)
        if response.status_code == 200:
            res_imgs.append(f'Ok: {img_src}')
            resps.append(response)
        if response.status_code == 404:
            counter += 1
            res_imgs.append(f'Broken: {img_src}')
            resps.append(response)

    all_imgs = dict(zip(resps, res_imgs))
    final_str = f'\nFrom {len(imgs)} images on img section: {counter} images are broken:'

    for key, val in all_imgs.items():
        final_str += f'\n{val} {key}'

    assert final_str, 'All images are ok'
    print(final_str)


@pytest.mark.positive
def test_select_all_checkboxes(driver, exp_wait):
    driver.get(URLS.heroku_4)

    page_header = exp_wait.until(ec.presence_of_element_located(HerokuApp.header_h3))
    assert page_header.text == 'Checkboxes'

    checkboxes = driver.find_elements(*HerokuApp.checkboxes)

    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()
            time.sleep(2)
        checkbox.click()
        time.sleep(2)
        assert checkbox.is_selected(), 'Checkbox is not selected'


@pytest.mark.positive
def test_one_checkbox_checked(driver, exp_wait):
    driver.get(URLS.heroku_4)

    page_header = exp_wait.until(ec.presence_of_element_located(HerokuApp.header_h3))
    assert page_header.text == 'Checkboxes'

    checkboxes = driver.find_elements(*HerokuApp.checkboxes)

    for checkbox in checkboxes:
        if checkbox.is_selected():
            print(f'\nCheckbox is checked')
        else:
            print(f'\nCheckbox is not checked')
        time.sleep(2)

    assert checkboxes[0].is_selected() or checkboxes[1].is_selected(), 'Wrong selection'


@pytest.mark.positive
def test_is_checkbox_checked(driver, exp_wait):
    driver.get(URLS.heroku_4)

    page_header = exp_wait.until(ec.presence_of_element_located(HerokuApp.header_h3))
    assert page_header.text == 'Checkboxes'

    checkbox_1 = driver.find_elements(*HerokuApp.checkboxes)[0]
    assert checkbox_1.get_attribute('checked') is None, 'Checked'

    checkbox_2 = driver.find_elements(*HerokuApp.checkboxes)[1]
    assert checkbox_2.get_attribute('checked'), 'Not checked'
