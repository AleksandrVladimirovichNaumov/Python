# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys

bakery = open('bakery.csv', 'r+', encoding='utf-8')
for i in range(int(sys.argv[1])-1):
    line = bakery.readline()
bytes_qnty = bakery.tell()
line = bakery.readline()
if len(line) == 0:
    print(f'{sys.argv[1]} is wrong number of a line')
else:
    bakery.seek(bytes_qnty)
    bakery.write(f'{sys.argv[2] + " " * (len(line)-len(sys.argv[2]))}')
bakery.closed