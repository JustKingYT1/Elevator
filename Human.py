from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, weigth):
        self.weigth = weigth

    @abstractmethod
    def unit_weigth(self):
        pass


class Passenger(Human):
    def __init__(self, weigth, location, floor):
        super().__init__(weigth)
        self.location = location
        self.floor = floor

    def unit_weigth(self):
        return self.weigth

    def unit_location(self):
        return self.location

    def exit_floor(self):
        return self.floor
