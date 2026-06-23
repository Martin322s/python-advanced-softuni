class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.index = len(obj)

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index -= 1

        if self.index >= 0:
            return self.obj[self.index]
        else:
            raise StopIteration