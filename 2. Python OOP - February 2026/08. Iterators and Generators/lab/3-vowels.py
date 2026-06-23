class vowels:
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, str):
        self.str = str
        self.current = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1

        if self.current < len(self.str):
            if self.str[self.current] in vowels.vowels:
                return self.str[self.current]
            else:
                return self.__next__()
        else:
            raise StopIteration