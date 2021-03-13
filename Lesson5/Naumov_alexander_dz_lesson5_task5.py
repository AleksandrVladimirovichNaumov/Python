# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
import random
import time

# creating list with random int
list_int = [random.randint(1, 20) for n in range(1, random.randint(50, 100))]
print(list_int)
# creating list with unique items from list_int
time_start = time.perf_counter()
list_unique_items = [list_int[n] for n in range(0, len(list_int)) if list_int.count(list_int[n]) == 1]
print(f'list with unique items from generator: {list_unique_items} \n time spent: {time.perf_counter() - time_start}')
# optimized algorithm
time_start = time.perf_counter()
temporary_set = set()
uniq_set = set()
for i in list_int:
    if i not in temporary_set:
        uniq_set.add(i)
    else:
        uniq_set.discard(i)
    temporary_set.add(i)
print(f'list with unique items from set: {uniq_set} \n time spent: {time.perf_counter() - time_start}')
