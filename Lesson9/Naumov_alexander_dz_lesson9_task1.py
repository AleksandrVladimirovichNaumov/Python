# Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time


class TrafficLight:
    # constructor
    # objects attributes
    def __init__(self, c):
        self.__color = c

    # methods
    def running(self):
        self.__color = 'red'
        print(self.__color, end='')
        for i in range(7):
            time.sleep(1)
            print('.', end='')
        print('')
        self.__color = 'yellow'
        print(self.__color, end='')
        for i in range(2):
            time.sleep(1)
            print('.', end='')
        print('')
        self.__color = 'green'
        print(self.__color, end='')
        for i in range(7):
            time.sleep(1)
            print('.', end='')
        print('\n')
        self.__color = ''


traffic_light_1 = TrafficLight('')
traffic_light_1.running()
