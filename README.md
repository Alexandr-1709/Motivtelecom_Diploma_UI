
## Проект UI автотестов Motivtelecom.ru

<!-- Технологии -->
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

### Тестируемый функционал
* Проверка авторизации с невалидными данными 
  (параметризованный тест)
* Проверка поиска по полному названию товара
* Поиск товара по категориям (параметризованный тест)
* Добавление товаров в корзину авторизованным пользователем
* Удаление всех товаров из корзины



### <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/Motivtelecom/)

##### Для запуска тестов кликнуть "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenoid.
![This is an image](images/screenshots/Jenkins.jpg)

<!-- Allure report -->

### <img width="5%" title="Allure Report" src="images/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/Motivtelecom/45/allure/)
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/Allure_Report_Over.jpg)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/Allure_Report_Graphs.jpg)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshots/Allure_Report_Suites.jpg)

##### Видео прохождение теста
![This is an image](images/screenshots/Test_Shop_Cart.gif)

<!-- Allure TestOps -->

### <img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/3583/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики и диаграммы.
![This is an image](images/screenshots/Allure_TestOps_Graphs.jpg)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/Allure_TestOps_test_cases.jpg)


<!-- Jira -->

### <img width="5%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно передать результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/Jira_integrationns.jpg)


<!-- Telegram -->

### <img width="5%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/telegram_report.jpg)