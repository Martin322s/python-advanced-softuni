class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)

        with open('results.txt', 'a') as file:
            file.write(f"Function {self.func.__name__} was called. Result: {result}\n")