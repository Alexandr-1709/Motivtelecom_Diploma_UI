import allure
from motivtelecom.model import app
from motivtelecom.model.helper.parametrize import authorization_with_params
from tests.conftest import home_page_only
from allure_commons.types import Severity

# @home_page_only
# def test_confirm_region():
#     with allure.step('Подтверждение региона'):
#         app.main_page.open_page()
#         app.main_page.confirm_region()


@home_page_only
@allure.tag("WEB UI")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Nikiforov")
def test_transition_to_login_page(driver_management_remote):
    with allure.step('Открытие в браузере главной страницы'):
        app.main_page.open_page()

    with allure.step('Переход на страницу авторизации'):
        app.login_page.open_login_page()

    with allure.step('Проверка нахождения на странице авторизации'):
        app.login_page.check_transition_to_login_page()


@home_page_only
@authorization_with_params
@allure.tag("WEB UI")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Nikiforov")
@allure.title('Авторизация пользователя по номеру телефона')
def test_authorization(phone_number, password, error_text):
    # GIVEN
    with allure.step('Переход на страницу авторизации'):
        app.main_page.open_page()
        app.login_page.open_login_page()

    # WHEN
    with allure.step('Ввод номер телефона'):
        app.login_page.input_phone_number(phone_number)

    with allure.step('Ввод пароль'):
        app.login_page.input_password(password)

    with allure.step('Подтверждение авторизации-кнока "Войти"'):
        app.login_page.click_submit()

    # THEN
    with allure.step('Проверка текста сообщения об ошибке'):
        app.login_page.check_error_message(error_text)
