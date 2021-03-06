# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [10, 58.5, 29.87, 5.3, 5.08, 12, 56, 58.14, 58.69, 73.2, 58, 36.3, 99.5, 47, 23, 54, 58.06]

print('initial list:\n', price_list, '\n', '_' * 510, '\n\n with applied format printed as a string:')
# formating and printing list to string in cycle
for i in price_list:
    print(f'{int(i)} руб {(str(float(i)) + "00")[str(float(i)).index(".") + 1:str(float(i)).index(".") + 3]} коп, ',
          end='')

print('\n_________________________________________________________________________________________________\n\nsorted'
      ' by increasing in same a list:')
print(f'\n id {id(price_list)} before sorting')
price_list.sort()
print(f'\n id {id(price_list)} after sorting is same')

for i in price_list:
    print(f'{int(i)} руб {(str(float(i)) + "00")[str(float(i)).index(".") + 1:str(float(i)).index(".") + 3]} коп, ',
          end='')

print('\n_________________________________________________________________________________________________\n\nsorted'
      ' by decreasing in a new list:')
for i in sorted(price_list, reverse=True):
    print(f'{int(i)} руб {(str(float(i)) + "00")[str(float(i)).index(".") + 1:str(float(i)).index(".") + 3]} коп, ',
          end='')
print(f'\n id before sorting {id(price_list)} != id after sorting {id(sorted(price_list))}')
print('\n_________________________________________________________________________________________________\n\n'
      'the most expensive five items:')
for index, i in enumerate(sorted(price_list, reverse=True)):
    print(f'{int(i)} руб {(str(float(i)) + "00")[str(float(i)).index(".") + 1:str(float(i)).index(".") + 3]} коп, ',
          end='')
    if index == 4:
        break
