class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0 - step

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += self.step

        if self.count:
            self.count -= 1
            return self.current
        else:
            raise StopIteration