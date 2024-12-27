from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования выполнения функции.
    """

    def wrapper(func):
        """Функция, которая принимает другую функцию
        func
         в качестве аргумента."""

        @wraps(func)
        def inner(*args, **kwargs):
            """Функция, которая принимает аргумент
            arg и kwargs"""

            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(f"{message}")
            else:
                if filename:
                    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(f"{message}")
                return result

        return inner

    return wrapper
