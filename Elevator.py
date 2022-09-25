import logging
import random
import time


class RestoreElevatorError(Exception):
    def __init__(self, text):
        self.text = text


class NumberFloorError(Exception):
    def __init__(self, text):
        self.text = text


class WeigthCapacityError(Exception):
    def __init__(self, text):
        self.text = text


# noinspection PyBroadException
class Elevator:
    def __init__(self, floors_count, elevator_capacity):
        self.unit = []
        self.floors_count = floors_count
        self.elevator_location = 1
        self.elevator_capacity = elevator_capacity
        self.weigth = 0
        self.exit_floor = 0
        self.unit_location = 0
        self.units = []
        self.waiting_units = []
        self.weigth_units = 0
        self.count_units = 0
        self.waiting_weigth_units = 0
        self.waiting_count_units = 0

    def move(self, number_floor):
        if self.weigth_units <= self.elevator_capacity:
            if number_floor <= self.floors_count:
                self.elevator_location = number_floor
            else:
                logging.critical("A message of CRITICAL severity")
                raise NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logging.warning("A WARNING")
            raise WeigthCapacityError("Вес выше допустимого")

    def add_waiting_unit(self, unit: list):
        if self.unit_location <= self.floors_count:
            self.unit = unit
            self.exit_floor = unit[0]
            self.weigth = unit[1]
            self.unit_location = unit[2]
            self.waiting_units.append(unit)
            self.waiting_count_units += 1
            print(f"Этаж на котором человек ожидает лифт: {self.unit_location}\nЭтаж на котором человек выйдет: "
                  f"{self.exit_floor}\nВес пассажира и его багажа, если он есть: {self.weigth}кг\n")
        else:
            logging.critical("A message of CRITICAL severity")
            raise NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")

    def delete_waiting_unit(self, i=0):
        while i < self.waiting_count_units:
            if self.elevator_location == self.waiting_units[i][2]:
                self.waiting_count_units -= 1
                self.waiting_units.pop(i)
                print("Очередь уменьшилась на 1\n")
            i += 1

    def add_unit(self, i=0):
        while i < self.waiting_count_units:
            if self.elevator_location == self.waiting_units[i][2]:
                self.weigth_units += weigth
                self.count_units += 1
                self.units.append(self.waiting_units[i])
                print("Человек зашел!\n")
            i += 1

    def delete_unit(self, i=0):
        while i < self.count_units:
            if self.elevator_location == self.units[i][0]:
                self.count_units -= 1
                self.weigth_units -= self.weigth
                self.units.pop(i)
                print("Человек вышел!\n")
            i += 1

    def to_ride(self, number_floor, i=0):
        self.move(number_floor)
        print(f'Мы прибыли на {number_floor} этаж\n')
        self.add_unit()
        try:
            while i < self.count_units + 100:
                self.delete_waiting_unit()
                self.delete_unit()
                i += 1
        except:
            pass
        return number_floor

    def check_waiting_units(self, i=0):
        try:
            while i < self.waiting_count_units + 100:
                print(f"{i + 1}:\nЭтаж на котором человек ожидает лифт: {self.waiting_units[i][2]}\nЭтаж куда едет "
                      f"пассажир: {self.waiting_units[i][0]}\nВес пассажира и его багажа,"
                      f" если он есть: {self.waiting_units[i][1]}кг\n")
                i += 1
        except:
            pass

    def check_units(self, i=0):
        try:
            while i < self.count_units + 100:
                print(
                    f"{i + 1}:\nЭтаж куда едет пассажир: {self.units[i][0]}\nВес пассажира и его багажа, если он есть:"
                    f" {self.units[i][1]}кг\n")
                i += 1
        except:
            pass

    @staticmethod
    def restore_elevator(i=10):
        print("Выполняется починка лифта, подождите 10 секунд\n")
        while i != 0:
            if i > 4:
                print(f"Идет починка лифта, осталось {i} секунд")
                time.sleep(1)
            elif i > 1:
                print(f"Идет починка лифта, осталось {i} секунды")
                time.sleep(1)
            else:
                print(f"Идет починка лифта, осталось {i} секунда")
                time.sleep(1)
            if i == 1:
                restore_num = random.randint(9, 10)
                if restore_num <= 9:
                    print("")
                    print("Лифт восстановлен успешно!\n")
                else:
                    print("")
                    raise RestoreElevatorError("Не удалось восстановить лифт, "
                                               "приносим свои извинения. Спасатели уже вызваны!")
            i -= 1

    def __str__(self):
        return f"Этаж на котором находится лифт: {self.elevator_location}\nОбщий вес лифта: {self.weigth_units}\n" \
               f"Количество пассажиров в ожидает: {self.waiting_count_units}\nКоличество пассажиров в " \
               f"лифте: {self.count_units}\n"


class Human:
    @staticmethod
    def call_elevator():
        return True


if __name__ == "__main__":
    capacity_elev = 1200
    floor_count_elev = 10
    elev = Elevator(floor_count_elev, capacity_elev)
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
                    raise NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
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
