# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить
# кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

my_list = ['в', '   5 ', 'часов', '17', ' минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('initial list:\n', my_list, '\n')

# variable for + or - before number
symbol = ''
# variable for skipping cycle steps after '"' addition
skip_till_index = 0

# formatting all list items in a cycle
for index, i in enumerate(my_list):
    # checking that skipping is required after addition of new '"' elements
    if index < skip_till_index:
        continue
    # delete all spaces before value
    i = i.lstrip()
    # delete all spaces after value
    i = i.rstrip()
    # checking + or - before number. if yes delete it from i and save in var symbol
    if i[0] == "+" or i[0] == "-":
        symbol = i[0]
        i = i[1:]
    # checking if it is a number
    if i.isdigit():
        # adding 0 before number if it is 1 symbol
        if len(i) < 2:
            i = i.zfill(2)
        # adding back a symbol
        my_list[index] = symbol + i
        # adding new list items '"' before and after a number
        my_list.insert(index, '"')
        my_list.insert(index + 2, '"')
        # skipping next two steps due to added to items in a list
        skip_till_index = index + 2
    else:
        # if not a number just add symbol if it was deleted and space in the end
        my_list[index] = symbol + i + ' '
    # making symbol empty for next cycle
    symbol = ''
print('list after modification:\n', my_list, '\n')
print('joined string:\n', "".join(my_list))
