import math

def sum(a, b):
    return a+b


if __name__ == '__main__':
    x = int(input())
    digits = []
    while x:
        digits = [x % 10] + digits
        print(digits)
        x = x // 10
    print(*digits)

