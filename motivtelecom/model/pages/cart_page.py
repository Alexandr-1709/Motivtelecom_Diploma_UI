import time

from selene.support.shared import browser
from allure import step
from selene import be, have


class CartPage:

    def remove_all_product_from_cart(self):
        with step('Удалить все товары из корзины'):
            browser.element('.card-basket__button').should(be.visible)
            items_for_remove = browser.all('.card-basket__button')

            while len(items_for_remove) > 0:
                browser.element('.card-basket__button').click()
                browser.wait_until(browser.element('.card-basket__button').should(be.clickable))



    def exit_from_cart(self):
        with step('Выйти из корзины'):
            browser.element('#logo-text').should(be.visible)
            browser.element('#logo-text').click()
            return self

    def check_empty_cart(self):
        with step('Проверить, что корзина пустая'):
            browser.element('.app-basket-empty'). \
                should(have.text('Ваша корзина пуста'))
            return self