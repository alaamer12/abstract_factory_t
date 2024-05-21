from __future__ import annotations
from abc import abstractmethod, ABC


class OSAPI(ABC):
    @abstractmethod
    def create_gui(self) -> GUI:
        pass

    @abstractmethod
    def create_cli(self) -> CLI:
        pass


class WindowsFactory(OSAPI):
    def create_gui(self) -> GUI:
        return WindowsGUI()

    def create_cli(self) -> CLI:
        return WindowsCLI()


class MACFactory(OSAPI):
    def create_gui(self) -> GUI:
        return MACGUI()

    def create_cli(self) -> CLI:
        return MACCLI()


class GUI(ABC):
    @abstractmethod
    def button(self):
        pass


class CLI(ABC):
    @abstractmethod
    def shell(self):
        pass


class WindowsGUI(GUI):
    def button(self):
        print("Windows button has been pressed.")


class WindowsCLI(CLI):
    def shell(self):
        print("Windows native shell has been created.")


class MACGUI(GUI):
    def button(self):
        print("MAC button has been pressed.")


class MACCLI(CLI):
    def shell(self):
        print("MAC native shell has been created.")


if __name__ == "__main__":
    windows_factory = WindowsFactory()
    windows_gui = windows_factory.create_gui()
    windows_cli = windows_factory.create_cli()
    windows_gui.button()
    windows_cli.shell()

    mac_factory = MACFactory()
    mac_gui = mac_factory.create_gui()
    mac_cli = mac_factory.create_cli()
    mac_gui.button()
    mac_cli.shell()
