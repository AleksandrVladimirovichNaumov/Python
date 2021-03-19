# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

# folders structure
project_folder_name = 'my_project'
project_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
# creating folders
try:
    os.mkdir(os.path.join(project_folder_name))
    for i in project_folders:
        os.mkdir(os.path.join(project_folder_name, i))
except Exception as e:
    print(f'global error: {e}')
