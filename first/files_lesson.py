with open('Nomenclature.txt', encoding='utf-8') as file:
    # text = file.read()
    lines = file.readlines()
    list_articuls = [[e.strip() for e in articul.split(',')] for articul in lines]
    dict_articuls = tuple(list_articuls)
    print(list_articuls)
    print(dict_articuls)