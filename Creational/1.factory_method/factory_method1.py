"""
Factory Method
Known as Virtual Constructor

Factory Method is a creational design pattern that provides an interface for creating
objects in a superclass, but allows subclasses to alter the type of objects that will be created.

"""

from abc import ABC, abstractmethod


# Creator
class Logistic(ABC):
    """
    1. Creating a Transport object
    2. Plan delivery
    """

    @abstractmethod
    def create_transportation(self):
        pass

    def plan_delivery(self):
        transport = self.create_transportation()
        return transport.deliver()


class RoadLogistic(Logistic):

    def create_transportation(self):
        return Truck()


class SeaLogistic(Logistic):

    def create_transportation(self):
        return Ship()


# Product
class Transport(ABC):

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):

    def deliver(self):
        return "Deliver by road"


class Ship(Transport):

    def deliver(self):
        return "Deliver by sea"


def client_code(logistic: Logistic):
    print(logistic.plan_delivery())


if __name__ == "__main__":
    sea_logistic = SeaLogistic()
    client_code(sea_logistic)

