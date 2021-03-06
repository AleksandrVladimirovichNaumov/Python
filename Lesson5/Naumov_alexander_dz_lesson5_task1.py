import random


def generator(max_number):
    """
    generator(max_number)
    :param max_number:
    :return: generator
    """
    for i in range(1, max_number + 1, 2):
        yield i
        print(f'next(odd_to_{max_number + 1}) \n {i}')


# making generator by function generator()
odd_numbers = generator(random.randint(2, 50))
# checking items in generator
print(*odd_numbers)
# checking type of generator
print(type(odd_numbers))
