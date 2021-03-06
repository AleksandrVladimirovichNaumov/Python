# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(*names):
    """
    thesaurus(*names)
    :param names:
    :return: dict (key - first latter of name from param names,  item - list of names starting from key letter)
    """

    # returned dictionary
    dict_of_names = {}
    # list of names starting from same letter
    list_of_names = []
    # how to get sorted dictionary of names
    namelist = sorted(list(names))
    # adding dictionary keys and items in a cycle
    for i in namelist:
        if not dict_of_names.get(i[0]):
            list_of_names.append(i)
            dict_of_names.setdefault(i[0], list_of_names)
        else:
            list_of_names = dict_of_names.get(i[0]).append(i)
            dict_of_names.setdefault(i[0], list_of_names)
        list_of_names = []
    return dict_of_names


# printing result of thesaurus() in a format from task
print(
    str(thesaurus("Иван", "Мария", "Илья", "Олег", "Михаил", "Ольга", "Инна", "Надежда")).replace('],',
                                                                                                  '],\n   ').replace(
        '{', '{\n    ').replace('}', '\n}'))
