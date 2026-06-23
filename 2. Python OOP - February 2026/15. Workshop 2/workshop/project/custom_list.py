from copy import deepcopy

class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def get_elements(self):
        return self.__data

    def append(self, value):
        self.__data.append(value)
        return self.__data
    
    def remove(self, index):
        return self.__data.pop(index)
    
    def get(self, index):
        return self.__data[index]
    
    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data
    
    def insert(self, index, value):
        self.__data.insert(index, value)
        return self.__data
    
    def pop(self):
        return self.__data.pop()
    
    def clear(self):
        self.__data.clear()

    def index(self, value):
        return self.__data.index(value)
    
    def count(self, value):
        return self.__data.count(value)
    
    def reverse(self):
        self.__data.reverse()
        return self.__data
    
    def copy(self):
        return deepcopy(self.__data)
    
    def size(self):
        return len(self.__data)
    
    def add_first(self, value):
        self.__data.insert(0, value)
        return None
    
    def dictionize(self):
        result = {}
        for i in range(0, len(self.__data), 2):
            key = self.__data[i]
            value = self.__data[i + 1] if i + 1 < len(self.__data) else " "
            result[key] = value
        return result
    
    def move(self, amount):
        if amount <= 0 or amount >= len(self.__data):
            return self.__data
        self.__data = self.__data[amount:] + self.__data[:amount]
        return self.__data
    
    def sum(self):
        total = 0
        for item in self.__data:
            if isinstance(item, (int, float)):
                total += item
            elif isinstance(item, str):
                total += len(item)
        return total
    
    def overbound(self):
        if not self.__data:
            return None
        max_value = max(self.__data, key=lambda x: len(str(x)) if isinstance(x, str) else x)
        return self.__data.index(max_value)
    
    def underbound(self):
        if not self.__data:
            return None
        min_value = min(self.__data, key=lambda x: len(str(x)) if isinstance(x, str) else x)
        return self.__data.index(min_value)