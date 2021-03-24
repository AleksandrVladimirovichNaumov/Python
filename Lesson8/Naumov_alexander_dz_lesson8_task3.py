# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    """
    type_logger(func)
    :param func:
    :return: wrapper. showing argument and its types of a function
    """
    print(type(func))

    def type_logger(*args, **kwargs):
        args_and_kwargs = list(args) + list(kwargs.values())
        types = tuple(map(lambda i: f'{i}: {type(i)}', args_and_kwargs))
        print(f'{func.__name__}{types}')
        orig_func = func(*args, **kwargs)
        return orig_func

    return type_logger


@type_logger
def sum_of_cubes(*args, **kwargs):
    """
    sum_of_cubes(*args)
    :param args:
    :return: summ of argument's cubes
    """
    result = 0
    try:
        for i in kwargs.values():
            result += i ** 3
        for i in args:
            result += i ** 3

        print(f'summ is {result}')
    except Exception as e:
        print(e)


sum_of_cubes(2, 3, a=2, b=3)
