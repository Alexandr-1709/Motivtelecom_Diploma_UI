from selene.support.shared import browser
from selene import have, be

class CartPage:

    def open_shoping_cart(self):
        ...





    def count_product_to_cart(self):
        quantity = browser.element('.app-total__title').locate().text
        return int(''.join(filter(str.isdigit, quantity)))
