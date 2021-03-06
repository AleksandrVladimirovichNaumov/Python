# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

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


def print_translation(original_word, translated_word):
    """
    print_translation(original_word, translated_word)
    :param original_word:
    :param translated_word:
    :return: printing two lines including parameters
    """
    print(f'>>> num_translate("{original_word}")\n"{translated_word}"')


def num_translate_adv(number):
    """
    num_translate_adv(number):
    :param number:
    :return: printing by print_translation() capitalized or lowered translation of imputed number
    """
    if number[0].isupper():
        print_translation(number, list_numbers.get(number.lower()).capitalize())
    else:
        print_translation(number, list_numbers.get(number))


# checking function for lower in a cycle
for i in list_numbers:
    num_translate_adv(i)

# checking function for capitalized in a cycle
for i in list_numbers:
    num_translate_adv(i.capitalize())

# checking result for item not in a dictionary
num_translate_adv('eleven')
