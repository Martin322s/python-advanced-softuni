class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise TypeError("Stack can store only strings!")
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack!")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        reversed_data = reversed(self.data)
        return "[" + ", ".join(reversed_data) + "]"