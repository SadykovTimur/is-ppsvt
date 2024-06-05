from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Component(id="mainFormTitle")
    logo = Component(id="headerLine_logo")
    menu = Component(id="MainMenuButton")
    save = Component(id="SaveButton")
    print = Component(id="PrintButton")
    got_url = Component(id="GotoURLButton")
    get_url = Component(id="GetURLButton")
    calculator = Component(id="CalculatorButton")
    calendar = Component(id="CalendarButton")
    set_buff = Component(id="SetBuffButton")
    add_buff = Component(id="AddBuffButton")
    sub_buff = Component(id="SubBuffButton")
    scale_form = Component(id="ScaleFormButton")
    show = Component(id="ShowTogetherButton")
    logout = Button(id="LogoutButton")
    menu_about = Button(id="MenuAboutButton")
    toolbar = Button(id="ToolbarCustMenuButton")

    @property
    def is_visible(self) -> bool:
        assert self.title.visible
        assert self.logo.visible
        assert self.menu.visible
        assert self.save.visible
        assert self.print.visible
        assert self.got_url.visible
        assert self.get_url.visible
        assert self.calculator.visible
        assert self.calendar.visible
        assert self.set_buff.visible
        assert self.add_buff.visible
        assert self.sub_buff.visible
        assert self.scale_form.visible
        assert self.show.visible
        assert self.logout.visible
        assert self.menu_about.visible

        return self.toolbar.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
