"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.color} цвета - {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, size):
        super().__init__(speed, color, name)
        self.size = size

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость машины {self.name} {self.color} цвета'
                  f' - {self.speed}. Вы превысили скорость!')
        else:
            print(f'Скорость машины {self.name} {self.color} цвета - {self.speed}')


class SportCar(Car):

    def __init__(self, speed, color, name, horsepower):
        super().__init__(speed, color, name)
        self.horsepower = horsepower


class WorkCar(Car):

    def __init__(self, speed, color, name, department):
        super().__init__(speed, color, name)
        self.department = department

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость машины {self.name} {self.color} цвета'
                  f' - {self.speed}. Вы превысили скорость!')
        else:
            print(f'Скорость машины {self.name} {self.color} цвета - {self.speed}')


class PoliceCar(Car):

    is_police = True


pol_car_1 = PoliceCar(75, 'Green', 'Ford')
pol_car_2 = PoliceCar(55, 'Black', 'Ford')

city_car_1 = TownCar(65, 'Blue', 'Golf', 'hetch')
city_car_2 = TownCar(35, 'Gold', 'Juke', 'crossover')

sport_auto = SportCar(100, name='Ferrari', color='Red', horsepower=750)

work_auto = WorkCar(50, 'White', 'Transporter', 'Rescuer')


city_car_1.show_speed()
print(city_car_1.go())
city_car_1.turn('налево')
city_car_1.stop()
print(city_car_1.size)
print(city_car_1.is_police)

print()

city_car_2.show_speed()
print(city_car_2.go())
city_car_2.turn('направо')
city_car_2.stop()
print(city_car_2.size)
print(city_car_2.is_police)

print()

pol_car_2.show_speed()
print(pol_car_2.go())
pol_car_2.turn('налево')
pol_car_2.stop()
print(pol_car_2.is_police)

print()

pol_car_1.show_speed()
print(pol_car_1.go())
pol_car_1.turn('направо')
pol_car_1.stop()
print(pol_car_1.is_police)

print()

sport_auto.show_speed()
print(sport_auto.go())
sport_auto.turn('налево')
sport_auto.stop()
print(sport_auto.horsepower)
print(sport_auto.is_police)

print()

work_auto.show_speed()
print(work_auto.go())
work_auto.turn('налево')
work_auto.stop()
print(work_auto.department)
print(work_auto.is_police)
