import allure
from motivtelecom.model import app
from motivtelecom.model.data.data_for_tests import full_name_product
from motivtelecom.model.helper.parametrize import categorys_params
from tests.conftest import shop_only


@shop_only
@allure.title('Проверка поиска по полному названию товара')
def test_full_name_search():
    # GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()
    # with allure.step('Перейти на страницу магазина'):
    #     app.motiv_shop_page.open_shop_page()
    with allure.step('Подтвердить регион'):
        app.motiv_shop_page.confirm_region_on_shop_page()

    # WHEN
    with allure.step('Ввести полное наименование товара в строку поиска'):
        app.motiv_shop_page.input_search_request(full_name_product)
    with allure.step('Перейти по первой ссылке в выпадающих подсказках'):
        app.motiv_shop_page.follow_the_first_hint()

    # THEN
    with allure.step('Проверка перехода на страницу товаров из поискового запроса'):
        app.product_page.check_title_product()


@shop_only
@categorys_params
@allure.title('Проверка поиска товара по категориям')
def test_search_product_from_category(category):
    # GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()
    # with allure.step('Перейти на страницу магазина'):
    #     app.motiv_shop_page.open_shop_page()
    with allure.step('Подтвердить регион'):
        app.motiv_shop_page.confirm_region_on_shop_page()

    # WHEN

    with allure.step('Перейти в выбранную категорию товара'):
        app.product_page.open_product_category(category)
    with allure.step('Проверка перехода на страницу товаров из категории поиска'):
        app.product_page.check_title_category(category.upper())


@shop_only
@allure.title('Добавление товаров в корзину из "Хиты продаж"')
def test_add_product_to_cart():
    # GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()
    # with allure.step('Перейти на страницу магазина'):
    #     app.motiv_shop_page.open_shop_page()
    with allure.step('Подтвердить регион'):
        app.motiv_shop_page.confirm_region_on_shop_page()

    # WHEN
    with allure.step('Добавить товары в корзину'):
        app.motiv_shop_page.added_product_from_hits()

    # THEN
    with allure.step('Проверка количества товаров в корзине'):
        app.motiv_shop_page.check_quantity_product_to_cart()
