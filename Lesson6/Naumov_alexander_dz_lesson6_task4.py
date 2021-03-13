#  Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
#  (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
#  Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные
#  в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

names = open('users.csv', 'r', encoding='utf-8')
hobbies = open('hobby.csv', 'r', encoding='utf-8')
names_and_hobbies = open('users_hobby.txt', 'w', encoding='utf-8')

# writing names and hobbies in *.txt line by line
for name in names:
    hobby = hobbies.readline().removesuffix('\n')
    name = name.removesuffix('\n')
    if hobby != '':
        names_and_hobbies.write(f"{name}: {hobby}\n")
    else:
        names_and_hobbies.write(f"{name}: None\n")

names.closed
hobbies.closed
names_and_hobbies.closed
