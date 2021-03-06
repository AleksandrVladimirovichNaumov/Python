# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# int variable for upper limit of a list
max_number = 1000
# int variable with value of a first odd number
start_number = 1
# list variable for odd numbers in a power of 3
odd_list = []
# list variable for odd numbers in a power of 3 + 17
odd_list17 = []
# sum of numbers which can be divided by 7 without excess
sum_of_zero_excess_list_1 = 0
sum_of_zero_excess_list_2 = 0
sum_of_zero_excess_list_1_plus_7 = 0
# making list of odd numbers in a power of 3
while start_number <= max_number:
    odd_list.append(start_number ** 3)
    start_number += 2

print(odd_list)

# calculating sum of numbers which can be divided by 7 without excess
# code includes only arithmetic operation as required in a task
for i in odd_list:

    working_item = i
    qnty_of_numbers = 0
    sum_of_i = 0
    n = 0

    # find a quantity of numbers in i
    while working_item:
        working_item = int(working_item / 10)
        qnty_of_numbers += 1
    print(f'quantity of numbers in "{i}" is {qnty_of_numbers}')

    # calculation sum of numbers of i
    working_item = i
    while n < qnty_of_numbers:
        sum_of_i += int(working_item / 10 ** (qnty_of_numbers - n - 1))
        print(f'sum of  {n + 1} first number(s) of "{i}" is {sum_of_i}')
        working_item -= int(working_item / 10 ** (qnty_of_numbers - n - 1)) * 10 ** (qnty_of_numbers - n - 1)
        print('working_item: ', working_item)
        n += 1

    print(f'sum of all number in {i} is {sum_of_i}')

    # sum i if excess is 0 after dividing by 7
    if sum_of_i / 7 - int(sum_of_i / 7) == 0:
        sum_of_zero_excess_list_1 += i
        print(f'      ****** "{i}" can be divided by 7 with zero excess *****')
print("_______________________________________________________________________________________________________________")
print('sum of all items from a list with zero excess after dividing by 7: ', sum_of_zero_excess_list_1)

# making new list where all items is bigger by 17
for i in odd_list:
    odd_list17.append(i + 17)

print(odd_list17)

# repeating all code for for odd_list17
for i in odd_list17:

    working_item = i
    qnty_of_numbers = 0
    sum_of_i = 0
    n = 0

    # find a quantity of numbers in i
    while working_item:
        working_item = int(working_item / 10)
        qnty_of_numbers += 1
    print(f'quantity of numbers in "{i}" is {qnty_of_numbers}')

    # calculation sum of numbers of i
    working_item = i
    while n < qnty_of_numbers:
        sum_of_i += int(working_item / 10 ** (qnty_of_numbers - n - 1))
        print(f'sum of  {n + 1} first number(s) of "{i}" is {sum_of_i}')
        working_item -= int(working_item / 10 ** (qnty_of_numbers - n - 1)) * 10 ** (qnty_of_numbers - n - 1)
        print('working_item: ', working_item)
        n += 1

    print(f'sum of all number in {i} is {sum_of_i}')

    # sum i if excess is 0 after dividing by 7
    if sum_of_i / 7 - int(sum_of_i / 7) == 0:
        sum_of_zero_excess_list_2 += i
        print(f'      ****** "{i}" can be divided by 7 with zero excess *****')
print("_______________________________________________________________________________________________________________")
print('sum of all items from a second list with zero excess after dividing by 7: ', sum_of_zero_excess_list_2)

# how to make same task (adding 17 to each item from a list) without creating a new list
for i in odd_list:

    # difference
    working_item = i + 17
    qnty_of_numbers = 0
    sum_of_i = 0
    n = 0

    # find a quantity of numbers in i
    while working_item:
        working_item = int(working_item / 10)
        qnty_of_numbers += 1
    # difference
    print(f'quantity of numbers in "{i + 17}" is {qnty_of_numbers}')

    # calculation sum of numbers of i
    # difference
    working_item = i + 17
    while n < qnty_of_numbers:
        sum_of_i += int(working_item / 10 ** (qnty_of_numbers - n - 1))
        # difference
        print(f'sum of  {n + 1} first number(s) of "{i + 17}" is {sum_of_i}')
        working_item -= int(working_item / 10 ** (qnty_of_numbers - n - 1)) * 10 ** (qnty_of_numbers - n - 1)
        print('working_item: ', working_item)
        n += 1

    # difference
    print(f'sum of all number in {i + 17} is {sum_of_i}')

    # sum i if excess is 0 after dividing by 7
    if sum_of_i / 7 - int(sum_of_i / 7) == 0:
        # difference
        sum_of_zero_excess_list_1_plus_7 += i + 17
        # difference
        print(f'      ****** "{i + 17}" can be divided by 7 with zero excess *****')
print("_______________________________________________________________________________________________________________")
print('sum of all items from a first list with zero excess after dividing by 7: ', sum_of_zero_excess_list_1)
print('sum of all items from a second list (+17 to each item) with zero excess after dividing by 7: ',
      sum_of_zero_excess_list_2)
print('sum of all items from a first list with added 17 and with zero excess after dividing by 7 and : ',
      sum_of_zero_excess_list_1_plus_7)
