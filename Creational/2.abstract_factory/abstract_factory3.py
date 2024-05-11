"""

Abstract Factory
Car => Benz, BMW => SUV, Coupe
    Benz suv => gla, glc
    BMW suv => x1, x2

    Benz Coupe => cls, E-class
    bmw coupe => m2, m4
"""
from abc import ABC, abstractmethod


class Car(ABC):
    pass


class Coupe(Car):
    @abstractmethod
    def get_info(self):
        pass


class Suv(Car):
    @abstractmethod
    def get_info(self):
        pass


class Gla(Suv):
    def get_info(self):
        return "Benz Suv Gla"


class Glc(Suv):
    def get_info(self):
        return "Benz Suv Glc"


class Cls(Coupe):
    def get_info(self):
        return "Benz Coupe Cls"


class EClass(Coupe):
    def get_info(self):
        return "Benz Coupe E-Class"


class X1(Suv):
    def get_info(self):
        return "BMW Suv X1"


class X2(Suv):
    def get_info(self):
        return "BMW Suv X2"


class X3(Suv):
    def get_info(self):
        return "BMW Suv X3"


class M2(Coupe):
    def get_info(self):
        return "BMW Coupe M2"


class M4(Coupe):
    def get_info(self):
        return "BMW Coupe M4"


class Factory(ABC):
    coupe_models = None
    suv_models = None

    @abstractmethod
    def create_coupe(self, model) -> Coupe:
        pass

    @abstractmethod
    def create_suv(self, model) -> Suv:
        pass


class Benz(Factory):
    coupe_models = {"cls": Cls, "e-class": EClass}
    suv_models = {"gla": Gla, "glc": Glc}

    def create_coupe(self, model):
        car_class = self.coupe_models.get(model)
        if not car_class:
            raise ValueError("Model is not supported!")
        return car_class()

    def create_suv(self, model):
        car_class = self.suv_models.get(model)
        if not car_class:
            raise ValueError("Model is not supported!")
        return car_class()


class BMW(Factory):
    coupe_models = {"m2": M2, "m4": M4}
    suv_models = {"x1": X1, "x2": X2, "x3": X3}

    def create_coupe(self, model):
        car_class = self.coupe_models.get(model)
        if not car_class:
            raise ValueError("Model is not supported!")
        return car_class()

    def create_suv(self, model):
        car_class = self.suv_models.get(model)
        if not car_class:
            raise ValueError("Model is not supported!")
        return car_class()


def client_code_coupe(factory: Factory, model):
    car = factory.create_coupe(model)
    result = car.get_info()
    print(result)


def client_code_suv(factory: Factory, model):
    car = factory.create_suv(model)
    result = car.get_info()
    print(result)


if __name__ == "__main__":
    bmw = BMW()
    client_code_coupe(bmw, "m2")
    client_code_suv(bmw, "x3")
