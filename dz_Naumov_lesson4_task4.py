# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.


import Utils

currencies = ['EUR', "usd", 'GbP', 'Bitkoin']

for i in currencies:
    print(Utils.currency_rates(i)[0], ',', Utils.currency_rates(i)[1])
