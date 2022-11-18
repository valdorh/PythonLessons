
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]

squares = [e*e for e in range(10) if e % 2 == 0]

text = "hello world"
words = [word.capitalize() for word in text.split()]

ints = [-1, 5, 0, -3, 9, -4]
positives = [n for n in ints if n > 0]

if __name__ == '__main__':
    list_str = f"*{squares}"
    print(str)
    print(*words)
    print(*positives)