import random
from Elevator import Elevator
from Human import Human
from Exceptions import Exceptions as ex


if __name__ == "__main__":
    capacity_elev = 1200
    floor_count_elev = 10
    elev = Elevator(floor_count_elev, capacity_elev)
    human = Human()
    while True:
        num_elev_location = elev.elevator_location
        print("1 - Вызов лифта\n2 - Передвижение лифта\n3 - Информация о лифте\n4 - Выключить лифт\n")
        number = int(input("Введите число соответствующее команде лифта -> "))
        print("")
        if number == 1:
            print("Лифт вызван!")
            print("")
            Human.call_elevator()
            if Human.call_elevator():
                unit_location = int(input("Введите этаж куда вызывается лифт -> "))
                print("")
                if unit_location <= floor_count_elev:
                    while True:
                        print("1 - Добавление пассажира\n2 - Завершить добавление пассажиров\n")
                        num1 = int(input("Введите число соответствующее команде лифта -> "))
                        print("")
                        if num1 == 1:
                            floor = int(input("Введите этаж куда поедет пассажир, который вызвал лифт -> "))
                            weigth = int(input("Введите вес пассажира и его багажа, если он есть, который вызвал лифт"
                                               " -> "))
                            print('')
                            elev.add_waiting_unit([floor, weigth, unit_location])
                        elif num1 == 2:
                            elev.move(num_elev_location)
                            break
                        else:
                            print("Неверно введена команда, повторите попытку")
                            print("")
                else:
                    raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        elif number == 2:
            break_num = random.randint(9, 10)
            num_floor = int(input("Введите номер этажа куда поедет лифт -> "))
            print("")
            if break_num <= 9:
                elev.to_ride(num_floor)
            elif break_num == 10:
                print("Лифт сломался, вызовите поддержку для починки лифта!\n")
                while True:
                    print("1 - Вызов поддержки, для починки лифта\n")
                    num2 = int(input("Введите число соответствующее команде лифта -> "))
                    print("")
                    if num2 == 1:
                        Elevator.restore_elevator()
                        break
                    else:
                        print("Неверно введена команда повторите попытку\n")
        elif number == 3:
            print("Ожидающие пассажиры\n")
            elev.check_waiting_units()
            print("Пассажиры в лифте\n")
            elev.check_units()
            print(elev)
        elif number == 4:
            print("Спокойной ночи")
            break
        else:
            print("Неверно введен номер команды, повторите попытку\n")
