"""

family of furniture like chair, sofa, Coffee table
for example products like chair+sofa+coffee table are available in these variants: Modern, Victorian, ArtDeco

"""

from abc import ABC, abstractmethod


class Chair(ABC):

    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_down(self):
        pass


class VictorianChair(Chair):
    def has_legs(self):
        print("Legs of victorian chair")

    def sit_on(self):
        print("Sitting on a victorian chair")


class VictorianSofa(Sofa):
    def lie_down(self):
        print("Lie down on victorian sofa")


class ModernChair(Chair):
    def has_legs(self):
        print("Legs of modern chair")

    def sit_on(self):
        print("Sitting on a modern chair")


class ModernSofa(Sofa):
    def lie_down(self):
        print("Lie down on modern sofa")


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


if __name__ == "__main__":
    furniture_family = "Modern"
    furniture_factory_mapper = {"Modern": ModernFurnitureFactory(), "Victorian": VictorianFurnitureFactory()}
    furniture_factory = furniture_factory_mapper.get(furniture_family)
    chair = furniture_factory.create_chair()
    sofa = furniture_factory.create_sofa()
    chair.has_legs()
    sofa.lie_down()
