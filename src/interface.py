from elevator import Elevator
from human import Passenger as p
from exceptions import Exceptions as ex

capacity_elev = 1200
floor_count_elev = 10
elev = Elevator(floor_count_elev, capacity_elev)
num_elev_location = elev.elevator_location


class Interface:
    def __init__(self):
        pass

    def menu(self):
        while True:
            print("1 - Вызов лифта\n2 - Передвижение лифта\n3 - Развезти пассажиров по этажам\n"
                  "4 - Информация о лифте\n5 - Выключить лифт\n")
            number = int(input("Введите число соответствующее команде лифта -> "))
            print("")
            if number == 1:
                self.call_elevator()
            elif number == 2:
                self.move()
            elif number == 3:
                self.auto_mover()
            elif number == 4:
                self.check_condition()
            elif number == 5:
                self.switch_off_elevator()
            else:
                print("Неверно введен номер команды, повторите попытку\n")

    @staticmethod
    def call_elevator():
        print("Лифт вызван!")
        print("")
        unit_location = int(input("Введите этаж куда вызывается лифт -> "))
        print("")
        if unit_location <= floor_count_elev:
            while True:
                print("1 - Добавление пассажира\n2 - Завершить добавление пассажиров\n")
                num1 = int(input("Введите число соответствующее команде лифта -> "))
                print("")
                if num1 == 1:
                    floor = int(input("Введите этаж куда поедет пассажир, который вызвал лифт -> "))
                    weigth = int(input("Введите вес пассажира и его багажа, если он есть, который вызвал лифт -> "))
                    print('')
                    passenger = p(weigth, unit_location, floor)
                    elev.add_waiting_units(passenger)
                elif num1 == 2:
                    elev.move(num_elev_location)
                    break
                else:
                    print("Неверно введена команда, повторите попытку")
                    print("")
        else:
            raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")

    @staticmethod
    def move():
        num_floor = int(input("Введите номер этажа куда поедет лифт -> "))
        print("")
        elev.to_ride(num_floor)

    @staticmethod
    def auto_mover():
        elev.auto_move_for_wait_units()
        elev.auto_move_for_units()
        pass

    @staticmethod
    def check_condition():
        print("Ожидающие пассажиры:\n")
        elev.check_waiting_units()
        print("Пассажиры в лифте:\n")
        elev.check_units()
        elev.check_elevator_condition()

    @staticmethod
    def switch_off_elevator():
        print("Спокойной ночи!")
        exit()


interface = Interface()
