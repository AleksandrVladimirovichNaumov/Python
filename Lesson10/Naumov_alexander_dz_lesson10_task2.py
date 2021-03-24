# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.
import abc


class Cloths(abc.ABC):

    @abc.abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Cloths):
    def __init__(self, v):
        self.V = v

    def size_hieght(self):
        return self.V

    def fabric_consumption(self):
        return self.V / 6.5 + 0.5


class Suit(Cloths):
    def __init__(self, hieght):
        self.hieght = hieght

    @property
    def hieght(self):
        return self.__hieght

    @hieght.setter
    def hieght(self, hieght):
        # if height imputed in meters
        if 0.75 < hieght < 2.5:
            self.__hieght = hieght
        # if height inputed in [cm] need to convert to [m]
        elif 250 > hieght > 75:
            self.__hieght = hieght/100
        else:
            print("incorrect height please enter in [cm] or [m]")


    def fabric_consumption(self):
        return self.hieght * 2 + 0.3


black_coat = Coat(48)
blue_suit = Suit(175)

print(black_coat.fabric_consumption())
print(blue_suit.fabric_consumption())