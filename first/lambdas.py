def square(x):
    return x ** 2


# square2 = lambda x: x ** 2

if __name__ == '__main__':
    a = 2
    result = lambda x=a: x ** 2
    a = 3
    result1 = lambda x=a: x ** 2
    print(result1())
    print(result())
    print("=" * 10)
    ints = list(range(21))
    res = filter(lambda x: x % 2 == 0, ints)
    # [print(e) for e in res if e % 5 == 0]
    a_dict = dict(a=3, b=2, d=1, c=4)
    print(sorted(a_dict.items(), key=lambda x: x[0]))
