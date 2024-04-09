import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from locators import URLS, MainLocks


@pytest.fixture()
def options():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    # chrome_options.add_argument("--headless")
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    return options


@pytest.fixture()
def driver(options):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def imp_wait(driver):
    driver.implicitly_wait(20)
    return imp_wait


@pytest.fixture()
def exp_wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


@pytest.fixture()
def form_conditions(driver):
    driver.get(URLS.main_url)

    login = driver.find_element(*MainLocks.login_field)
    passw = driver.find_element(*MainLocks.pass_field)
    checkbox = driver.find_element(*MainLocks.checkbox)

    if checkbox.is_selected() or login.text != '' or passw.text != '':
        checkbox.click()
        login.clear()
        passw.clear()

    assert login.text == '', 'Not empty'
    assert passw.text == '', 'Not empty'
    assert not checkbox.is_selected(), 'Selected'

    yield form_conditions
