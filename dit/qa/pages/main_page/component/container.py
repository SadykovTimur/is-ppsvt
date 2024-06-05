from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Container']


class ContainerWrapper(ComponentWrapper):
    title = Text(css='[class="toplineBox"]')
    content = Component(css='[class*="gridContent"]')
    title_column = Text(css='[class="dots"]')

    @property
    def is_visible(self) -> bool:
        assert self.command in 'Начальная страница'
        assert self.content.visible
        assert self.title_column in 'Потребности'

        return self.title_column in 'Текущие дела'


class Container(Component):
    def __get__(self, instance, owner) -> ContainerWrapper:
        return ContainerWrapper(instance.app, self.find(instance), self._locator)
