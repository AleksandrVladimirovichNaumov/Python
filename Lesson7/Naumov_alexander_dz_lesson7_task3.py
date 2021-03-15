# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

template_ext = '.html'
templates_list = []
templates_folder = 'templates'
import os
import shutil

# making root folder
try:
    os.mkdir(templates_folder)
except Exception as e:
    print(f'Global exception: {e}')
# making list with html files and it adress and folder name. not creating a folder for templates because
# it will be included during  os.walk
for root, folders, files in os.walk(os.path.abspath(os.curdir)):
    for i in files:
        if i.lower().find(template_ext) == len(i) - len(template_ext):
            templates_list.append([root, root.split('\\')[-3], i])
# creating sub folders for html files
for root, folder, file in templates_list:
    try:
        os.mkdir(os.path.join(templates_folder, folder))
    except Exception as e:
        print(f'Global exception: {e}')
    try:
        shutil.copyfile(f'{root}\\{file}', os.path.join(templates_folder, folder, file))
    except Exception as e:
        print(f'Global exception: {e}')