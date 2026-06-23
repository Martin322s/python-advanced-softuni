from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area():
        return None
    
    @abstractmethod
    def calculate_perimeter():
        return None
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, height, width):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__height * self.__width
    
    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)
