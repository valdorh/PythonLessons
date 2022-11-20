def squares():
    print("Generator working...")
    for e in range(0, 11, 2):
        yield e ** 2


def pause():
    print('Generator working...')
    while True:
        # print(a)
        yield a


if __name__ == '__main__':
    # gen = squares()
    # for e in gen:
    #     print(e)
    a = 10
    gen = pause()
    print(next(gen))
    a = 1050
    print(next(gen))
