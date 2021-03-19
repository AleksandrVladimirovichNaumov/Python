# Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# my_project:
#   settings:
#     - __init__.py
#     - dev.py
#     - prod.py
#   mainapp:
#     - __init__.py
#     - models.py
#     - views.py
#     - templates:
#         - mainapp:
#             - base.html
#             - index.html
#   authapp:
#     - __init__.py
#     - models.py
#     - views.py
#     - templates:
#         - mainapp:
#             - base.html
#             - index.html
#
#
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя

import os

# making a list of strins from config file
with open('config.yaml', encoding='utf-8') as config:
    lines = config.readlines()


# function to make a folder
def make_dir(folder_name, *paths):
    """
    make_dir(folder_name, *paths)
    :param folder_name:
    :param paths: folder starting from script root folder
    :return: create a folder
    """
    try:
        os.mkdir(os.path.join(*paths, folder_name))
    except Exception as e:
        print(f'Global error: {e}')


def make_file(file_name, *paths):
    """
    make_file(file_name, *paths)
    :param file_name:
    :param paths: folder starting from script root folder
    :return: create a file
    """
    try:
        new_file = open(os.path.join(*paths, file_name), 'w', encoding='utf-8')
        new_file.closed
    except Exception as e:
        print(f'Global error: {e}')


def format_file_name(file):
    """
    format_file_name(file)
    :param file:
    :return: formated file's name
    """
    file = file.strip()
    file = file.replace('- ', '')
    return file


def format_dir_name(dir):
    """
    format_dir_name(dir)
    :param dir:
    :return: formated folder's name
    """
    dir = dir.strip()
    dir = dir.replace('- ', '')
    dir = dir[:dir.find(':')]
    return dir


# dict for folder in main directory
dirs = {}

# checking every line from a config file
for i in lines:
    print(i)
    # root folder of file
    if not i.startswith(' ' * 2):
        if i.find(':') > 0:
            make_dir(format_dir_name(i))
            dirs[1] = format_dir_name(i)
        else:
            make_file(format_file_name(i))
    # lvl 1 folders & files (folder & files in root directory)
    elif i.startswith(' ' * 2) and not i.startswith(' ' * 4):
        if i.find(':') > 0:
            make_dir(format_dir_name(i), dirs[1])
            dirs[2] = format_dir_name(i)
        else:
            make_file(format_file_name(i), dirs[1])
    # lvl 2 folders & files (folder & files in lvl 1 folder)
    elif i.startswith(' ' * 4) and not i.startswith(' ' * 6):
        if i.find(':') > 0:
            make_dir(format_dir_name(i), dirs[1], dirs[2])
            dirs[3] = format_dir_name(i)
        else:
            make_file(format_file_name(i), dirs[1], dirs[2])
    # lvl 3 folders & files (folder & files in lvl 2 folder)
    elif i.startswith(' ' * 8) and not i.startswith(' ' * 10):
        if i.find(':') > 0:
            make_dir(format_dir_name(i), dirs[1], dirs[2], dirs[3])
            dirs[4] = format_dir_name(i)
        else:
            make_file(format_file_name(i), dirs[1], dirs[2], dirs[3])
    # lvl 4 folders & files (folder & files in lvl 3 folder)
    elif i.startswith(' ' * 12) and not i.startswith(' ' * 14):
        if i.find(':') > 0:
            make_dir(format_dir_name(i), dirs[1], dirs[2], dirs[3], dirs[4])
            dirs[5] = format_dir_name(i)
        else:
            make_file(format_file_name(i), dirs[1], dirs[2], dirs[3], dirs[4])
