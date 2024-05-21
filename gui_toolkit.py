from __future__ import annotations
from abc import abstractmethod, ABC


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MACFactory(GUIFactory):
    def create_button(self) -> Button:
        return MACButton()

    def create_checkbox(self) -> Checkbox:
        return MACCheckbox()


class Button(ABC):
    @abstractmethod
    def pressed(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def checked(self):
        pass


class WindowsButton(Button):
    def pressed(self):
        print("Windows button pressed")


class MACButton(Button):
    def pressed(self):
        print("MAC button pressed")


class WindowsCheckbox(Checkbox):
    def checked(self):
        print("Windows checkbox checked")


class MACCheckbox(Checkbox):
    def checked(self):
        print("MAC checkbox checked")


if __name__ == "__main__":
    windows_factory = WindowsFactory()
    button = windows_factory.create_button()
    checkbox = windows_factory.create_checkbox()
    button.pressed()
    checkbox.checked()

    factory = MACFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.pressed()
    checkbox.checked()
