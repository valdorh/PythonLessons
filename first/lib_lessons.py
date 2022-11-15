def learn_dict_29_ex1():
    inp = "one=1 two=2 three=3"
    lst = list(inp.split())
    tmp_lst = [y.split("=") for y in lst]
    for i in range(len(tmp_lst)):
        tmp_lst[i][1] = int(tmp_lst[i][1])
    d = dict(tmp_lst)
    print(*sorted(d.items()))


def learn_dict_29_ex2():
    lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
    d = {}
    for item in lst_in:
        lst_item = item.split('=')
        d[int(lst_item[0])] = lst_item[1]
    print(*sorted(d.items()))


def learn_dict_29_ex3():
    str_inp = "вологда=город house=дом True=1 5=отлично 9=божественно"
    lst = str_inp.split()
    print(lst)
    d = {}
    for item in lst:
        key, value = item.split('=')
        d[key] = value
    if 'house' in d and 'True' in d and '5' in d:
        print("ДА")


def learn_dict_29_ex4():
    str_inp = "лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина"
    d = dict(i.split('=') for i in str_inp.split())
    if "False" in d:
        del d["False"]
    if '3' in d:
        del d['3']
    print(*sorted(d.items()))
