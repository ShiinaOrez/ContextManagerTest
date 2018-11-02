from functools import wraps

def contextManager(func):
    class decorated_func:
        def __enter__(self):
            self.maker = func()
            return next(self.maker)

        def __exit__(self, exc_type, exc_value, traceback):
            try:
                next(self.maker)
            except StopIteration:
                print("---Shiina---Over!")
            finally:
                del self.maker

    return decorated_func
