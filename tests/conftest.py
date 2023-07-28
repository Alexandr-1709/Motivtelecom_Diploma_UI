import os
import pickle
import time
from allure import step
import pytest
#from selene import browser
from selene.support.shared import browser
from dotenv import load_dotenv

from motivtelecom.model import app
from motivtelecom.model.data import data_for_tests
from motivtelecom.utils import attach
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function',
                params=[(data_for_tests.base_url, data_for_tests.shop_url)],
                autouse=True)
def driver_management_remote(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        keep_alive=True,
        options=options,
    )

    browser.config.driver = driver
    browser.config.hold_driver_at_exit = False
    browser.config.base_url = request.param
    browser.config.shop_url = request.param
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 5.0

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


shop_only = pytest.mark.parametrize('driver_management_remote',
                                    [data_for_tests.shop_url],
                                    indirect=True
                                    )

home_page_only = pytest.mark.parametrize('driver_management_remote',
                                         [data_for_tests.base_url],
                                         indirect=True
                                         )


@pytest.fixture()
def record_auth_cookies(load_env, driver_management_remote):
    phone = os.getenv('user_phone')
    password = os.getenv('user_password')

    app.main_page.open_page()

    app.motiv_shop_page. \
        open_autorization_page(). \
        go_to_open_autorization_page(). \
        input_phone(phone). \
        input_password(password). \
        click_submit_auth()

    pickle.dump(browser.driver.get_cookies(), open('authorization_cookies', 'wb'))


@pytest.fixture()
def auth_through_cookies(record_auth_cookies):
    for cookie in pickle.load(open('authorization_cookies', 'rb')):
        browser.driver.add_cookie(cookie)
    time.sleep(5.0)
    browser.driver.refresh()
    with step('Проверить bvkjfv;'):
        browser.element('.user-tooltip__link').click()
    time.sleep(10.0)
