from gui_toolkit import WindowsFactory, MACFactory
from os_api import WindowsFactory as WF, MACFactory as MF
from furniture_manufacturer import GermanFurniture, ItalianFurniture

if __name__ == '__main__':
    match i := input("1. Windows GUI\n2. Windows CLI\n3. German\n4. Italian\n Choose: "):
        case "1":
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

        case "2":
            windows_factory = WF()
            windows_gui = windows_factory.create_gui()
            windows_cli = windows_factory.create_cli()
            windows_gui.button()
            windows_cli.shell()

            mac_factory = MF()
            mac_gui = mac_factory.create_gui()
            mac_cli = mac_factory.create_cli()
            mac_gui.button()
            mac_cli.shell()

        case "3":
            german_furniture = GermanFurniture()
            italian_furniture = ItalianFurniture()

            german_furniture.make_chair().sculpture()
            german_furniture.make_chair().paint()
            german_furniture.paint_table().sculpture()
            german_furniture.paint_table().paint()

            italian_furniture.make_chair().sculpture()
            italian_furniture.make_chair().paint()
            italian_furniture.paint_table().sculpture()
            italian_furniture.paint_table().paint()
        case _:
                print("Wrong input")
                exit(0)
