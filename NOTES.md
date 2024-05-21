# About
this design pattern is unique because is bottomless, u can extend it as much u want , Although this will increase the complexity and space usage too much.

there are different levels in this pattern 
- Abstracted levels:
  - in this level the abstracted class can be one or more [depending on the level and complexity]
  - e.g. [PlatformFactory -> OSFactory]
- Concrete Factories levels:
  - in this level, those are the factories that u want to provide or implement, but they do not have any implementations
  - e.g. [WindowsFactory, MACFactory]
- concrete Client levels:
  - in this level where u concrete[implement] the smallest parts of the system
  - also this level can be one or more
  - e.g. [WindowsGUI, WindowsCLI, MACGUI, MACCLI]
  - and [WindowsGui -> WindowsButton, WindowsCheckbox]
  - and [MACGui -> MACButton, MACCheckbox]
  - and so on

# Procedures
1. define the top level [most abstracted class or classes] 
2. define the concrete [factories] that you want to use
3. define the concrete [clients] that you want to use
4. create the most abstract class as abc class
    1. if its more than one level do the step 4.0 again for each level
   2. create the concrete [factories] that you want to use also make their return type the abstract thing u are targeting like Button, Chair, etc.
   and make them inherit step 4.1 based on the levels in step 4.0 and 4.1
   3. create those targeting classes but the abstracted versions like Button, Chair, etc.
   and also make them abc classes
   4. create concrete client classes that implement the targeted classes
   so u are going to inherit from step 4.4
   5. unlike the Factory pattern there is no class for client so usually u will write the client [classes and methods calling] in the `main` function
   6. write the [main] function
   7. call the [main] function

# Note:
i dont know if it can be a client class but so far i think no
    

# Example
```python
from __future__ import annotations
from abc import abstractmethod, ABC


class PlatformFactory(ABC):
    @abstractmethod
    def create_os_factory(self) -> OSFactory:
        pass


class OSFactory(ABC):
    @abstractmethod
    def create_gui(self) -> GUI:
        pass

    @abstractmethod
    def create_cli(self) -> CLI:
        pass


# Windows implementations
class WindowsFactory(PlatformFactory):
    def create_os_factory(self) -> OSFactory:
        return WindowsOSFactory()


class WindowsOSFactory(OSFactory):
    def create_gui(self) -> GUI:
        return WindowsGUI()

    def create_cli(self) -> CLI:
        return WindowsCLI()


# MAC implementations
class MACFactory(PlatformFactory):
    def create_os_factory(self) -> OSFactory:
        return MACOSFactory()


class MACOSFactory(OSFactory):
    def create_gui(self) -> GUI:
        return MACGUI()

    def create_cli(self) -> CLI:
        return MACCLI()


# GUI and CLI interfaces and implementations
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
    windows_platform_factory = WindowsFactory()
    windows_os_factory = windows_platform_factory.create_os_factory()
    windows_gui = windows_os_factory.create_gui()
    windows_cli = windows_os_factory.create_cli()
    windows_gui.button()
    windows_cli.shell()

    mac_platform_factory = MACFactory()
    mac_os_factory = mac_platform_factory.create_os_factory()
    mac_gui = mac_os_factory.create_gui()
    mac_cli = mac_os_factory.create_cli()
    mac_gui.button()
    mac_cli.shell()

```