# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationety:

    # attributes
    def __init__(self, t):
        self.title = t

    # methods
    def draw(self):
        print("Draw starts.")


class Pen(Stationety):

    # attributes
    def __init__(self, t):
        super().__init__(t)

    # methods
    def draw(self):
        print("Pen starts.")


class Pencil(Stationety):

    # attributes
    def __init__(self, t):
        super().__init__(t)

    # methods
    def draw(self):
        print("Pencil starts.")


class Handle(Stationety):

    # attributes
    def __init__(self, t):
        super().__init__(t)

    # methods
    def draw(self):
        print("Handle starts")


stationery_1 = Stationety("Flags kit")
pen_1 = Pen('Blue pen')
pencil_1 = Pencil('Red pencil')
handle_1 = Handle("Black handle")

stationery_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()
