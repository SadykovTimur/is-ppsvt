from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.component.container import Container
from dit.qa.pages.main_page.component.header import Header
from dit.qa.pages.main_page.component.panel import Panel

__all__ = ['MainPage']


class MainPage(Page):
    msg_btn = Button(css='[id*="messageBoxButton"]')
    logout = Button(id="LogoutCloseButton")
    exit_btn = Button(xpath="//button[text()='Завершить работу']")
    header = Header(id="headerLine")
    box = Component(id="themesCellLimiter")
    panel = Panel(id="instrCell")
    page = Container(id="pages")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible
                assert self.box.visible
                assert self.panel.is_visible

                return self.page.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
