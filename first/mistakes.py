

a_dict = {1: 1, 2: 2}

value = a_dict.get(3, None)  # Не правильно None по умолчанию
value = a_dict.get(3)
print(type(value))

integers = [e for e in range(1, 11)]  # Не правильно , излишне
integers = list(range(1, 11))
print(integers)

integers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
print(integers)
integers = [e ** 2 for e in range(10) if e % 2 == 0]
print(integers)

# print(sum(e for e in range(10_000_000) if e % 2 == 0))

for index, element in enumerate(integers, 1):
    print(f"{index} : {element}")

if len(integers) > 0:  # не желательно
    pass
if integers:  # тоже самое
    pass

# flag b all https://docs.python.org/3.8/library/functions.html#built-in-funcs
integers = [1, 4, 16, 36, 64]
flag = True
for integer in integers:
    if integer < 0:
        flag = False
        break
print(integers, flag)

print(all(e > 0 for e in integers))
