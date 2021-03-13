# 3.	Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель
# между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле,
# хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот —
# выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

names = open('users.csv', 'r', encoding='utf-8')
hobbies = open('hobby.csv', 'r', encoding='utf-8')
result_dict = {}


# creating dictionary key = name, value = hobby or None
for name in names:
    hobby = hobbies.readline()
    if hobby != '':
        result_dict[name.removesuffix('\n')] = hobby.removesuffix('\n')
    else:
        result_dict[name.removesuffix('\n')] = None

# checking that quantity of hobbies not less than names
if hobbies.readline() != '':
    print(1)
else:
    dict_to_txt = open('dict.txt', 'w', encoding = 'utf-8')
    dict_to_txt.write(str(result_dict))
    dict_to_txt.closed

names.closed
hobbies.closed
