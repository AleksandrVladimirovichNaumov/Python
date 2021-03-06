# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(number, unique=False):
    """
    get_jokes(number, unique = False)
    :param number: quantity of jokes
    :param unique: flag - words cannot be duplicated
    :return: return list of jokes generated from list of words
    """
    # final list of jokes
    list_of_jokes = []
    # string for 1 joke
    joke = ''
    # lists of words
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    # max quantity of uniques jokes
    max_unique_jokes = min(len(nouns), len(adverbs), len(adjectives))

    for i in range(1, number + 1):
        # unique flag off
        if not unique:
            list_of_jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        # unique jokes with correct number of jokes
        elif unique == True and number in range(1, 1 + max_unique_jokes):
            selected_word = random.choice(nouns)
            nouns.remove(selected_word)
            joke += selected_word + " "
            selected_word = random.choice(adverbs)
            adverbs.remove(selected_word)
            joke += selected_word + " "
            selected_word = random.choice(adjectives)
            adjectives.remove(selected_word)
            joke += selected_word + " "
            list_of_jokes.append(joke)
            joke = ''
        # not possible quantity of unique jokes
        else:
            list_of_jokes.append(
                f'{number} is wrong quantity of jokes (min = 1, max = {max_unique_jokes})')
            break
    # take back words meaning after deletion for unique jokes
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    return list_of_jokes


print('random quantity of not unique jokes')
print(get_jokes(random.randint(1, 10)))
print('max quantity of unique jokes')
print(get_jokes(5, True))
print('not possible quantity of uniques jokes')
print(get_jokes(6, True))
