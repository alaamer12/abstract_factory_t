from __future__ import annotations
from abc import abstractmethod, ABC


class FurnitureManufacturer(ABC):
    @abstractmethod
    def make_chair(self) -> Chair:
        pass

    def paint_table(self) -> Table:
        pass


class GermanFurniture(FurnitureManufacturer):
    def make_chair(self) -> Chair:
        return GermanChair()

    def paint_table(self) -> Table:
        return GermanTable()


class ItalianFurniture(FurnitureManufacturer):
    def make_chair(self) -> Chair:
        return ItalianChair()

    def paint_table(self) -> Table:
        return ItalianTable()


class Chair(ABC):
    @abstractmethod
    def sculpture(self) -> None:
        pass

    @abstractmethod
    def paint(self) -> None:
        pass


class Table(ABC):
    @abstractmethod
    def sculpture(self) -> None:
        pass

    @abstractmethod
    def paint(self) -> None:
        pass


class GermanChair(Chair):
    def sculpture(self) -> None:
        print("German chair sculpture")

    def paint(self) -> None:
        print("German chair painting")


class GermanTable(Table):
    def sculpture(self) -> None:
        print("German table sculpture")

    def paint(self) -> None:
        print("German table painting")


class ItalianChair(Chair):
    def sculpture(self) -> None:
        print("Italian chair sculpture")

    def paint(self) -> None:
        print("Italian chair painting")


class ItalianTable(Table):
    def sculpture(self) -> None:
        print("Italian table sculpture")

    def paint(self) -> None:
        print("Italian table painting")


if __name__ == "__main__":
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
