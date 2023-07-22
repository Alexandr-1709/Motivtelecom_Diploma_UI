from selene.support.shared import browser
from selene import have, be, command
from allure import step

class MotivShopPage:

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
        hits_element = browser.element('.main-page__hits')
        hits_element.should(be.visible)
        items_for_add = hits_element.all('card__footer-basket')
        with step('Накидать товаров в корзину'):
            for item in items_for_add:
                #item.element('.card__footer-basket').should(be.visible)
                item.click()
                browser.element('.tingle-modal__button-close').should(be.visible)
                browser.element('.tingle-modal__button-close').click()
