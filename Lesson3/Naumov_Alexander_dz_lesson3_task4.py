# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*names_surnames):
    """
    thesaurus_adv(*names_surnames)
    :param names_surnames:
    :return: dict with first letter of surname as a key, and dict (same as in previous task) as a item
    """

    # returned dictionary
    dict_of_surnames = {}
    # adding dictionary keys and items in a cycle
    for i in names_surnames:
        if not dict_of_surnames.get(i[i.index(' ') + 1]):
            dict_of_surnames.setdefault(i[i.index(' ') + 1], thesaurus(i))
        else:
            if not dict_of_surnames.get(i[i.index(' ') + 1]).get(i[0]):
                dict_of_surnames.setdefault(i[i.index(' ') + 1],
                                            (dict_of_surnames.get(i[i.index(' ') + 1])).setdefault(i[0],
                                                                                                   thesaurus(i).get(
                                                                                                       i[0])))
            else:
                dict_of_surnames.get(i[i.index(' ') + 1]).get(i[0]).append(thesaurus(i).get(i[0])[0])
    return dict_of_surnames


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
    str(thesaurus_adv("Иван Иванов", "Мария Иванчук", "Петр Сазонов", "Илья Иванько", "Олег Сергеев", "Михаил Круг",
                      "Ольга Петрова", "Инна Карелина", "Надежда Шимко", "Игнат Иродов", "Олег Приходько")).replace(
        ": [", ":\n       [").replace("], ", "],\n    ").replace("}, '", "},\n '").replace(": {", "'\n    {"))
