# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
import random
# creating list of int
list_of_int = [random.randint(1, 500) for n in range(1, random.randint(15, 30))]
print(list_of_int)
# creating generator from list_of_int where all items is bigger than previous item in list_of_int
list_of_bigger_int = (list_of_int[n] for n in range(1, len(list_of_int)) if list_of_int[n] > list_of_int[n - 1])
print(*list_of_bigger_int)
