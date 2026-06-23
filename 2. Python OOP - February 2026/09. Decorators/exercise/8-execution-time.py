import time

def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        
        total_time = end_time - start_time
        
        return total_time
    return wrapper