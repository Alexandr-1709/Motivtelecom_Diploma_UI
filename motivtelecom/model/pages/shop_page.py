from selene.support.shared import browser
from selene import be, command, have
from allure import step


class MotivShopPage:

    def __init__(self):
        self.count_product = 0
        self.count_before_add = 0


    def open_autorization_page(self):
        with step('Открыть страницу авторизации'):
            browser.element('.header-main__services-item .js-modal').click()
            return self

    def go_to_open_autorization_page(self):
        with step('Перейти на страницу авторизации'):
            browser.element('.tingle-modal-box .authorization__link_password'). \
                should(be.visible)
            browser.element('.tingle-modal-box .authorization__link_password'). \
                click()
            return self

    def input_phone(self, phone_number):
        with step('Ввести номер телефона'):
            collection = browser.all('#personal-phone-js')
            collection.second.should(be.visible)
            collection.second.click()
            collection.second.type(phone_number)
            return self

    def input_password(self, password):
        with step('Ввести пароль'):
            element = browser.element('.tingle-modal--visible .authorization__wrapper')
            element.element('#fp-password-js').should(be.visible)
            element.element('#fp-password-js').click()
            element.element('#fp-password-js').type(password)
            return self

    def click_submit_auth(self):
        with step('Подтвердить авторизацию - кнока "Войти"'):
            element = browser.element('.tingle-modal--visible .authorization_password')
            element.element('.form-phone-password__submit-button').click()
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
        collection = browser.all('.catalog-result .card__footer-basket')
        items_for_add = collection.by(have.exact_text('В корзину'))

        self.count_product = len(items_for_add)

        with step('Накидать товаров в корзину'):
            for item in items_for_add:
                item.click()
                browser.element('.tingle-modal__button-close').should(be.visible)
                browser.element('.tingle-modal__button-close').click()


    def count_product_to_cart(self):
        quantity = browser.element('.js-info-basket .products-button__counter'). \
            locate().text
        return int(''.join(filter(str.isdigit, quantity)))

    def check_quantity_product_to_cart(self):
        quantity = browser.element('.js-info-basket .products-button__counter'). \
            locate().text
        count_after_add = int(''.join(filter(str.isdigit, quantity)))
        browser.element('.js-info-basket .products-button__counter').\
            perform(command.js.scroll_into_view)
        print(count_after_add, self.count_before_add, self.count_product)
        assert (count_after_add - self.count_before_add) == self.count_product

    def open_cart(self):
        with step('Открыть страницу с выбранным товаром'):
            browser.element('.js-info-basket').click()


