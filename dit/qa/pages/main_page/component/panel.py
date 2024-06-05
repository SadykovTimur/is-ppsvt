from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Panel']


class PanelWrapper(ComponentWrapper):
    command = Component(id="cmd_commandsMenu")
    favorites = Component(id="cmd_favoritesMenu")
    history = Component(id="cmd_historyMenu")
    search = Component(id="cmd_searchMenu")
    notification = Component(id="cmd_notificationsMenu")

    @property
    def is_visible(self) -> bool:
        assert self.command.visible
        assert self.favorites.visible
        assert self.history.visible
        assert self.search.visible

        return self.notification.visible


class Panel(Component):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)
