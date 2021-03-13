# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных файлов
# и имя выходного файла. Проверить работу скрипта.

# console command for script from Therminal
# python Naumov_alexander_dz_lesson6_task5.py users.csv hobby.csv dict_console2.txt


import sys
names_txt = str(sys.argv[1])
hobbies_txt = str(sys.argv[2])
users_hobbies_txt = str(sys.argv[3])
names = open(names_txt, 'r', encoding='utf-8')
hobbies = open(hobbies_txt, 'r', encoding='utf-8')
names_and_hobbies = open(users_hobbies_txt, 'w', encoding='utf-8')

# writing in a file line by line
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
