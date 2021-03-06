# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

employees_list = ['инженер-конструктор Игорь   ', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
employee_name = ''

# take name from a string and print message in a cycle
for i in employees_list:
    i = i.rstrip()  # deleting all spaces from end of string
    i = i[i.rfind(" "):]  # deleting everything before last space
    employee_name = i.title()  # make all letter low except a first one
    print(f'Привет,{employee_name}!')
