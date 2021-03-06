# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.

# dictionary for numbers
list_numbers = {'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}


def num_translate(number):
    """
    num_translate(number)
    :param number:
    :return: translation of a number in Russian from dict list_numbers
    """
    print(f'>>> num_translate("{number}")\n"{list_numbers.get(number)}"')


# checking function in a cycle
for i in list_numbers:
    num_translate(i)

# checking result for item not in a dictionary
num_translate(1)
