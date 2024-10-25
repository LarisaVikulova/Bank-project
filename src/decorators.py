def log(filename=""):
    """Декоратор, который логирует начало и конец выполнения функции, ее результаты и ошибки"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
        return wrapper
    return my_decorator
