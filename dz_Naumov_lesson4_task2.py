# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.
import requests
import requests.utils as utils


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # cutting all symbols before and after inputted currency rate
    working_str = content[content.find(currency.upper()):]
    working_str = working_str[:working_str.find('</Value')]
    working_str = working_str[working_str.find('Value>') + len('Value>'):]
    # converting rate to float or making result as None for not valid currency
    if not working_str == "":
        working_str = working_str.replace(',', '.')
        working_str = float(working_str)
    else:
        working_str = None
    return working_str


print(currency_rates("gbp"))
print(currency_rates("USD"))
print(currency_rates("Eur"))
print(currency_rates("Bitkoin"))
