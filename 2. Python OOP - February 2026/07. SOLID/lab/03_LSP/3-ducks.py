from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class BaseToy(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class RubberDuck(BaseToy):
    def make_sound(self):
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def quack(self):
        return "Robotic quacking"

    def walk(self):
        return "Robotic walking"

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0