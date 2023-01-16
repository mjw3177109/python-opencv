import time


def timing(func):
    def decorated(*args, **kwargs):
        start = time.time()
        res=func(*args, **kwargs)
        end = time.time()
        print(end - start, func.__name__)
        return res

    return decorated
