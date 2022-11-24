def outer(func):
    def inner(*args, **kwargs):
        print("Реклама")
        return func(*args, **kwargs)

    return inner


@outer
def div(a, b):
    return a / b


@outer
def mul(a, b):
    return a * b


if __name__ == '__main__':
    print(div(1, 2))
    print(mul(5, 6))
