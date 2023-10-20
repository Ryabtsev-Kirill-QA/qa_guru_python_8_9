import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("Ryabtsev-Kirill-QA/qa_guru_python_8_8").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("Ryabtsev-Kirill-QA/qa_guru_python_8_8")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 1"):
        s(by.partial_text("#1")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("Ryabtsev-Kirill-QA/qa_guru_python_8_8")
    go_to_repository("Ryabtsev-Kirill-QA/qa_guru_python_8_8")
    open_issue_tab()
    should_see_issue_with_number("#1")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
