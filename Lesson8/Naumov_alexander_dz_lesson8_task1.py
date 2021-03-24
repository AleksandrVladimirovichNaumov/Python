# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re

email = input("Input email: ")


def email_parse(email_adress):
    """
    email_parse(email_adress)
    :param email_adress: string with email adress
    :return: return dict with username and domain of an email if it correct
    """
    result_dict = {}
    msg = f'wrong email: {email_adress}'
    # for checking email adress
    # rules:
    # 1) username:
    #       - first symbol cannot be a dot ((?<!\.). it should be [A-Za-z0-9!#$%&'*+/=?^_`{|}~-]
    #       - next symbols (if they exist) [A-Za-z0-9!#$%&'*+/=?^_`{|}~-]*
    #       - last sybols cannot be a dot (?<!\.). checking it before '@'
    # 2) only 1 '@' is allowed
    # 3) domain:
    #       - before dot:
    #           - first symbol cannot be a number or '-'. it should be letters (?<![0-9-])[a-zA-Z]
    #           - next symbols( if they exist) [A - Za - z0 - 9-]*
    #           - last sybol cannot be '-'. checking before dot (?<![-])
    #       - only 1 dot is allowed
    #       - after dot: [a-zA-Z]+ // all letters
    RE_EMAIL = re.compile(
        r"^((?<!\.)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-][A-Za-z0-9!#$%&'*+./=?^_`{|}~-]*)(?<!\.)@((?<![0-9-])[a-zA-Z][a-zA-Z0-9-]*(?<![-])[.][a-zA-Z]+)$")

    if RE_EMAIL.match(email_adress):
        result_dict['username'] = RE_EMAIL.findall(email_adress)[0][0]
        result_dict['domain'] = RE_EMAIL.findall(email_adress)[0][1]
        return (result_dict)
    else:
        raise ValueError(msg)


print(email_parse(email), '\n')

wrong_emails = (
'.a@a.a', 'a.@a.a', 'a@@a.a', 'в@a.a', 'a@в.a', 'a@a.в', 'a*a.a', 'a@a_a', 'a@1a.a', 'a@-a.a', 'a@a-.a', 'a@a.1')

print('**************** Autocheck wrong emails ***********')
for i in wrong_emails:
    try:
        print(f'{i} = {email_parse(i)}')
    except Exception as e:
        print(e)

correct_emails = ('a.a@a.a', '!a@a.a', '!a!@a.a', 'a@a1a.a', 'a@a-a1.a')

print('\n**************** Autocheck correct emails ***********')
for i in correct_emails:
    try:
        print(f'{i} = {email_parse(i)}')
    except Exception as e:
        print(e)

