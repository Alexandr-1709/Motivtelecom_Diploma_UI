from selene.support.shared import browser
from selene import have, be
from motivtelecom.model.data.data_for_tests import full_name_product
import allure


class ProductPage:
    def check_title_product(self):
        browser.element('h1[class*="title-section_h1"]'). \
            should(have.text(full_name_product.upper()))
        return self

    def product_from_category_in_stock(self, product):
        with allure.step('Проверить найденный товар'):
            browser.element('.product-item').should(have.text(f'{product}'))

    def check_title_category(self, category):
        browser.element('h1[class*="title-section_h1"]'). \
            should(have.text(category))

    def open_product_category(self, category):
        browser.element('.header__bottom').should(be.visible)
        element = browser.element('.header__bottom')
        element.element("//a[contains(text(), '%s')]" % category).click()

    def notification_add_product_to_cart(self):
        with allure.step('Уведомление о добавлении товара в корзину'):
            element = browser.element('.tingle-modal')
            element.element('//h2[contains(text(),"Товар добавлен в корзину")]'). \
                should(be.visible)
            return self

    def close_notification_add_product_to_cart(self):
        with allure.step('Закрыть уведомление о добавлении товара в корзину'):
            browser.element('.tingle-modal__button-close').click()
            return self
