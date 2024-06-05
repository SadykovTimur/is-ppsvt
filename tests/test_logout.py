from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_DEVICE_TYPE

from dit.qa.constants import CLIENT_BROWSERS
from tests.steps import logout, open_main_page, open_start_page, sign_in


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('IS-PPSVT')
@allure.story('Выход из системы')
@allure.title('Проверка выхода из системы')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_logout(request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    logout(app)