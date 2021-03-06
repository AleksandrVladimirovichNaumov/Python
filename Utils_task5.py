# *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.

import requests
import requests.utils as utils
import datetime


def currency_rates(currency):
    """
    currency_rates(currency)
    :param currency: what currency rate is required
    :return: currency rate [float], date [date]
    """
    # preventing error if scrypt is runned not from Terminal
    if len(currency) < 2:
        return None
    # taking argument from list sys.argv
    currency = str(currency[1])
    # taking info from inet
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    working_str = content[content.find(currency.upper()):]
    # cutting all symbols before and after inputted currency rate
    working_str = working_str[:working_str.find('</Value')]
    working_str = working_str[working_str.find('Value>') + len('Value>'):]
    # converting rate to float or making result as None for not valid currency
    if not working_str == "":
        working_str = working_str.replace(',', '.')
        working_str = float(working_str)
    else:
        working_str = None
    # cutting everything before and after date
    date = content[content.find('Date="') + len('Date="'):]
    date = date[:date.find('"')]
    date = date.split('.')
    # converting string to date
    date = list(map(int, date))
    date = datetime.date(day=date[0], month=date[1], year=date[2])
    print(working_str, ',', date, sep='')
    return 0


if __name__ == '__main__':
    import sys
    exit(currency_rates(sys.argv))
