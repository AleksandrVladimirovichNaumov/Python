import requests
import requests.utils as utils
import datetime


def currency_rates(currency):
    """
    currency_rates(currency)
    :param currency: what currency rate is required
    :return: currency rate [float], date [date]
    """
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
    return working_str, date


currencies = ['EUR', "usd", 'GbP', 'Bitkoin']

if __name__ == '__main__':
    for i in currencies:
        print(currency_rates(i)[0], ', ', currency_rates(i)[1], sep='')
