# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import collections
import json


def size_group(size):
    """
    e_group(size)
    :param size:
    :return: upper limit half-integral 10
    """
    i = 1
    while size > 0:
        size //= 10
        i *=10
    return i


# folder to analyse
folder = input('Input a link to a folder: ')
# dict for results
files_dict = collections.defaultdict(list)
set1={}
try:
    # taking each object from imputed folder
    for file in os.listdir(folder):
        # checking that it is a file
        if os.path.isfile(f'{folder}\\{file}'):
            # getting size of a file
            file_size = os.path.getsize(f'{folder}\\{file}')
            # adding into a dictionary
            files_dict[size_group(file_size)].append(os.path.splitext(f'{folder}\\{file}')[1])
            # deleting duplicate of
            set1 = set(files_dict.get(size_group(file_size)))
            files_dict[size_group(file_size)] = (list(set1))
except Exception as e:
    print(f'Global exception: {e}')
# making json obj with files_dict
json_dict = json.dumps(files_dict)
# writing json onj to a file. Removesuffix is required if someone will input folder adress as E:/Python/Study/Lesson1/
with open(f'{folder.removesuffix("/").split("/")[-1]}_summary.json', 'w', encoding='utf-8') as file:
    file.write(json_dict)
