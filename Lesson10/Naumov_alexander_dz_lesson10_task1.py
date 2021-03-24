# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и пр.
import random
import itertools


class Matrix:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        matrix = ''
        # returning as a string
        for lines in self.values:
            matrix += f'{lines}\n'
        return matrix.replace('[', '').replace(',', '').replace(']', '').replace(' ', '\t')

    def __add__(self, other):
        # matrix there all items is a tuple (item_from_first_matrix, item_from_second_matrix)
        sum_matrix = []
        # matrix with result of matrix_1 + matrix_2
        result_matrix = []
        # temporary line for matrix creation
        line = []

        def line_generator(length):
            """
            line_generator(length):
            :param length:
            :return: list with required quantity of 0
            """
            empty_line = [0 for i in range(length)]
            return empty_line

        temp_matrix = list(itertools.zip_longest(self.values, other.values, fillvalue=line_generator(
            max(len(self.values[0]), len(other.values[0])))))
        # adding lines with required quantity of 0 if matrix1 and matrix2 are different size

        print('adding lines with required quantity of 0 if matrix1 and matrix2 are different size:')
        print(Matrix(temp_matrix))

        for i in temp_matrix:
            temp_line = list(itertools.zip_longest(*i, fillvalue=0))
            sum_matrix.append(temp_line)
        print('matrix with tuples from first and second matrix (zero columns are added if required)')
        print(Matrix(sum_matrix))

        for l in sum_matrix:
            for i in l:
                line.append(sum(i))
            result_matrix.append(line)
            line = []
        return Matrix(result_matrix)


def random_matrix(lines, columns):
    """
    random_matrix(lines, columns)
    :param lines:
    :param columns:
    :return: return a random matrix
    """
    matrix = []
    for i in range(lines):
        matrix.append([random.randint(0, 9) for n in range(columns)])
    return matrix


matrix_01 = Matrix(random_matrix(7, 2))
matrix_02 = Matrix(random_matrix(5, 5))
print('********************* First Matrix ***************************')
print(matrix_01)
print('********************* Second Matrix ***************************')
print(matrix_02)
print('********************* Summ of first and second matrices ***************************\n')
print(matrix_01.__add__(matrix_02))
