class countdown_iterator:
    def __init__(self, count):
        self.origianl_count = count + 1
        self.count = count + 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count -= 1
        if self.count < 0:
            self.count = self.origianl_count
            raise StopIteration
        return self.count