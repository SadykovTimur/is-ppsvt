from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    title = Text(css='[class*="Header"')
    login = TextField(id="userName")
    password = TextField(id="userPassword")
    submit = Button(id="okButton")
    cancel = Component(id="cancelButton")
    splash_img = Component(id="splashInterp")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title in '1С:Предприятие'
                assert self.login.visible
                assert self.password.visible
                assert self.submit.visible
                assert self.cancel.visible

                return self.splash_img.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
