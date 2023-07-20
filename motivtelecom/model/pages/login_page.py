from selene.support.shared import browser
from selene import have, be


class LoginPage:

    def open_login_page(self):
        browser.element('#icon_key').click()
        return self

    def input_phone_number(self, number):
        browser.element('.input-text-wrap [type="tel"]').click()
        browser.element('.input-text-wrap [type="tel"]').type(number)
        return self

    def input_password(self, password):
        browser.element('.auth-input[type="password"]').click()
        browser.element('.auth-input[type="password"]'). \
            type(password)
        return self

    def check_error_message(self, text):
        browser.element('.b-input-text__input-error'). \
            should(have.text(text))
        return self

    def click_submit(self):
        browser.element('.modal-btn-default[type="submit"]').click()
        return self

    def check_transition_to_login_page(self):
        browser.element('.modal-title').should(be.visible)
        return self
