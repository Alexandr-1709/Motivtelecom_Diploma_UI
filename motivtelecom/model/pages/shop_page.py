from selene.support.shared import browser
from selene import have, be


from motivtelecom.model.data.data_for_tests import full_name_product


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

    def check_title_product(self):
        browser.element('h1[class*="title-section_h1"]').\
            should(have.text(full_name_product.upper()))
        return self

    def confirm_region_on_shop_page(self):
        browser.element('//button[contains(text(),"Да, верно")]').should(be.visible)
        browser.element('//button[contains(text(),"Да, верно")]').click()
        return self
