from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['LogoutPage']


class LogoutPage(Page):
    title = Text(class_name='exitBox')
    repeat = Component(id="repeatEnter")
    logo = Component(class_name="exitImg")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title in 'АРМ ДИТ\nДо новых встреч!'
                assert self.repeat.visible

                return self.logo.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
