from enum import Enum
from selene.support.shared import browser
from selene import have

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










