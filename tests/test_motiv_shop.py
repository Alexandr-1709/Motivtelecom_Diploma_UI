import allure
from motivtelecom.model import app
from motivtelecom.model.data.data_for_tests import full_name_product


@allure.title('Проверка поиска по полному названию товара')
def test_full_name_search():
    #GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()
    with allure.step('Перейти на страницу магазина'):
        app.motiv_shop_page.open_shop_page()

    #WHEN
    with allure.step('Подтвердить регион'):
        app.motiv_shop_page.confirm_region_on_shop_page()
    with allure.step('Ввести полное наименование товара в строку поиска'):
        app.motiv_shop_page.input_search_request(full_name_product)
    with allure.step('Перейти по первой ссылке в выпадающих подсказках'):
        app.motiv_shop_page.follow_the_first_hint()

    #THEN
    with allure.step('Проверка соответствия заголовка товара, поисковому запросу'):
        app.motiv_shop_page.check_title_product()



