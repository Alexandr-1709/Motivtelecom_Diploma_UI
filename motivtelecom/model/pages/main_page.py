from enum import Enum
from selene.support.shared import browser



class Region(Enum):
    SVERDL_OBL = 'Свердловская область'
    KURGAN_OBL = 'Курганская область'
    HMAO_UGRA = 'Ханты-Мансийский автономный округ - Югра'
    YAMAL = 'Ямало-Ненецкий автономный округ'


class MainPage:

    def open_page(self):
        browser.open('')
        return self

    def confirm_region(self):
        browser.element('.b-header__choose-region-button-left').click()
        return self

    # def check_region_name(self):
    #     text = browser.element('.b-header__choose-region-text')
    #     text.at

    def open_shop_page(self):
        browser.element('.b-sections-menu__link-text_double').click()
        browser.switch_to_next_tab()
        return self
