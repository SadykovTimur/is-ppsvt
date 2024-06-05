import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.logout_page import LogoutPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'logout',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            page = MainPage(app)
            page.msg_btn.click()
            page.wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def logout(app: Application) -> None:
    with allure.step('Logout page'):
        try:
            main_page = MainPage(app)
            main_page.header.logout.click()
            main_page.logout.click()
            main_page.exit_btn.click()

            LogoutPage(app).wait_for_loading()

            screenshot_attach(app, 'logout_page')
        except Exception as e:
            screenshot_attach(app, 'logout_page_error')

            raise TimeoutError('Logout was not loaded') from e
