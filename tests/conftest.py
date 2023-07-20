import pytest
from selene import browser
from motivtelecom.utils import attach
from selenium import webdriver
import config
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='function', autouse=True)
def driver_managment_remote():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_height = False
    browser.config.base_url = 'https://motivtelecom.ru/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 15

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

# @pytest.fixture(scope='function', autouse=True)
# def driver_management():
#     browser.config.driver = webdriver.Remote(
#         config.settings.remote_url, options=config.settings.driver_options
#     )
#     browser.config.window_width = config.settings.window_width
#     browser.config.window_height = config.settings.window_height
#     browser.config.base_url = config.settings.base_url
#     browser.config.hold_driver_at_exit = config.settings.hold_driver_at_exit
#     browser.config.timeout = config.settings.timeout
#
#     yield
#
#     attach.add_html(browser)
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_video(browser)
#     browser.quit()