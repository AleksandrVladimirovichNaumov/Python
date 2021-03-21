# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    # attributes
    def __init__(self, s, c, n, i_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p

    # methods
    def go(self):
        print('Vehicle starts.')

    def stop(self):
        print('Vehicle stops.')

    def turn(self, direction):
        print(f"Vehicle turns {direction}")

    def show_speed(self):
        print(f'Speed is {self.speed}')


class TownCar(Car):
    # attributes
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)

    # methods
    def show_speed(self):
        speed_limit = 60
        if self.speed <= speed_limit:
            print(f'Speed is {self.speed}')
        else:
            print(f'Speed is {self.speed}. Please slow down. Speed limit is {speed_limit} km/hour.')


class SportCar(Car):
    # attributes
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)


class WorkCar(Car):
    # attributes
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)

    # methods
    def show_speed(self):
        speed_limit = 40
        if self.speed <= speed_limit:
            print(f'Speed is {self.speed}')
        else:
            print(f'Speed is {self.speed}. Please slow down. Speed limit is {speed_limit} km/hour.')


class PoliceCar(Car):
    # attributes
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)


town_car_1 = TownCar(95, 'red', 'Mad granny on VW Polo', False)
town_car_2 = TownCar(55, 'black', 'Taxi driver Abdul on Lada Granta', False)
sport_car_1 = SportCar(210, 'green', "Mayor's son on Porsche Panamera", False)
work_car_1 = WorkCar(100, 'brown', "'Nachalnika' on Kamaz", False)
work_car_2 = WorkCar(25, 'grey', "Michalych on 'Buchanka'", False)
police_car = PoliceCar(100, 'blue', 'Cop Bogdan on Ford Focus', True)

# checking story
def drive(car=town_car_1):
    """
    drive(car=town_car_1)
    :param car:
    :return: story of a ride
    """
    print(f'This is {car.name} in {car.color} color.')
    car.go()
    car.show_speed()
    car.turn('left')
    car.show_speed()
    print(f'Police is trying to stop {car.name}.')
    if car.is_police:
        print(f'{car.name} says "Hey, cop Vasya, WTF!?"')
    else:
        car.stop()


print('\n**************************************************************************\n')
drive(town_car_1)
print('\n**************************************************************************\n')
drive(town_car_2)
print('\n**************************************************************************\n')
drive(sport_car_1)
print('\n**************************************************************************\n')
drive(work_car_1)
print('\n**************************************************************************\n')
drive(work_car_2)
print('\n**************************************************************************\n')
drive(police_car)