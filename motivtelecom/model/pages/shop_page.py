from selene.support.shared import browser
from selene import have, be, command
from allure import step


class MotivShopPage:

    def __init__(self):
        self.count_product = None
        self.count_before_add = None

    def open_shop_page(self):
        browser.element('.b-sections-menu__link-text_double').click()
        browser.switch_to_next_tab()
        return self

    def input_search_request(self, name):
        browser.element('.vue-search__value').should(be.visible)
        browser.element('.vue-search__value').click()
        browser.element('.vue-search__value').type(name)
        return self

    def follow_the_first_hint(self):
        browser.element('.vue-search__link:first-child').click()
        return self

    def confirm_region_on_shop_page(self):
        browser.element('//button[contains(text(),"Да, верно")]').should(be.visible)
        browser.element('//button[contains(text(),"Да, верно")]').click()
        return self

    def added_product_from_hits(self):
        with step('Проскроллить до Хитов'):
            browser.element('.main-page__hits').perform(command.js.scroll_into_view)
        browser.element('// a[ @ href = "/catalog/hits/"][1]').click()

        self.count_before_add = self.count_product_to_cart()
        items_for_add = browser.all('.catalog-result .card__footer-basket')
        self.count_product = len(items_for_add)

        with step('Накидать товаров в корзину'):
            for item in items_for_add:
                item.click()
                browser.element('.tingle-modal__button-close').should(be.visible)
                browser.element('.tingle-modal__button-close').click()


    def count_product_to_cart(self):
        quantity = browser.element('//a[@href="/cart/" and @class="products-viewed__link app-popup-btn"]').\
            locate().text
        return int(''.join(filter(str.isdigit, quantity)))

    def check_quantity_product_to_cart(self):
        quantity = browser.element('//a[@href="/cart/" and @class="products-viewed__link app-popup-btn"]').\
            locate().text
        count_after_add = int(''.join(filter(str.isdigit, quantity)))
        assert (count_after_add - self.count_before_add) == self.count_product