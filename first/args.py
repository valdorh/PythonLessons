# a, *b = [4, 10], 12, 33, 56


# noinspection SpellCheckingInspection
def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} started")
        result = func(*args)
        print(f"{func.__name__} finished")
        return result

    return wrapper


@logger
def summ(a, b):
    return a + b


if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))
    # print("="*10)
    # print(logger(summ)(2, 3))
    print(summ(1, 6))