import logging
import random
import time
import json as j
from Exceptions import Exceptions as ex


# noinspection PyBroadException
class Elevator:
    def __init__(self, floors_count, elevator_capacity):
        self.elevator_broken = False
        self.num_break = 0
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
        with open("WaitingUnits.json", "r") as read_file:
            self.waiting_units = j.load(read_file)
        with open("WaitingUnitsCount.json", "r") as read_file:
            self.waiting_count_units = j.load(read_file)
        with open("Units.json", "r") as read_file:
            self.units = j.load(read_file)
        with open("UnitsWeigth.json", "r") as read_file:
            self.weigth_units = j.load(read_file)
        with open("UnitsCount.json", "r") as read_file:
            self.count_units = j.load(read_file)
        with open("ElevatorLocation.json", "r") as read_file:
            self.elevator_location = j.load(read_file)

    def move(self, number_floor):
        if not self.elevator_broken:
            if self.weigth_units <= self.elevator_capacity:
                if number_floor <= self.floors_count:
                    self.elevator_location = number_floor
                    with open("ElevatorLocation.json", "w") as write_file:
                        j.dump(self.elevator_location, write_file)
                else:
                    logging.critical("A message of CRITICAL severity")
                    raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
            else:
                logging.warning("A WARNING")
                raise ex.WeigthCapacityError("Вес выше допустимого")
        else:
            raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                          "приносим свои извинения. Спасатели уже вызваны!")

    def add_waiting_unit(self, unit: list):
        if not self.elevator_broken:
            if self.unit_location <= self.floors_count:
                self.unit = unit
                self.exit_floor = unit[0]  # Этаж на котором пассажир выйдет
                self.weigth = unit[1]  # Вес багажа и его пассажира
                self.unit_location = unit[2]  # местоположение ожидающего пассажира
                self.waiting_units.append(unit)
                self.waiting_count_units += 1
                with open("WaitingUnits.json", "w") as write_file:
                    j.dump(self.waiting_units, write_file)
                with open("WaitingUnitsCount.json", "w") as write_file:
                    j.dump(self.waiting_count_units, write_file)
                print(f"Этаж на котором человек ожидает лифт: {self.unit_location}\nЭтаж на котором человек выйдет: "
                      f"{self.exit_floor}\nВес пассажира и его багажа, если он есть: {self.weigth}кг\n")
            else:
                logging.critical("A message of CRITICAL severity")
                raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                          "приносим свои извинения. Спасатели уже вызваны!")

    def delete_waiting_unit(self, i=0):
        if not self.elevator_broken:
            while i < self.waiting_count_units:
                if self.elevator_location == self.waiting_units[i][2]:  # сравнение местоположения лифта с
                    # местоположением ожидающего пассажира
                    self.waiting_count_units -= 1
                    self.waiting_units.pop(i)
                    with open("WaitingUnits.json", "w") as write_file:
                        j.dump(self.waiting_units, write_file)
                    with open("WaitingUnitsCount.json", "w") as write_file:
                        j.dump(self.waiting_count_units, write_file)
                    print("Очередь уменьшилась на 1\n")
                i += 1
        else:
            raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                          "приносим свои извинения. Спасатели уже вызваны!")

    def add_unit(self, i=0):
        if not self.elevator_broken:
            while i < self.waiting_count_units:
                if self.elevator_location == self.waiting_units[i][2]:
                    self.weigth_units += self.waiting_units[i][1]
                    self.count_units += 1
                    self.units.append(self.waiting_units[i])
                    with open("Units.json", "w") as write_file:
                        j.dump(self.units, write_file)
                    with open("UnitsWeigth.json", "w") as write_file:
                        j.dump(self.weigth_units, write_file)
                    with open("UnitsCount.json", "w") as write_file:
                        j.dump(self.count_units, write_file)
                    print("Человек зашел!\n")
                i += 1
        else:
            raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                          "приносим свои извинения. Спасатели уже вызваны!")

    def delete_unit(self, i=0):
        if not self.elevator_broken:
            while i < self.count_units:
                if self.elevator_location == self.units[i][0]:
                    self.count_units -= 1
                    self.weigth_units -= self.units[i][1]
                    self.units.pop(i)
                    print("Человек вышел!\n")
                    with open("Units.json", "w") as write_file:
                        j.dump(self.units, write_file)
                    with open("UnitsWeigth.json", "w") as write_file:
                        j.dump(self.weigth_units, write_file)
                    with open("UnitsCount.json", "w") as write_file:
                        j.dump(self.count_units, write_file)
                i += 1
        else:
            raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                          "приносим свои извинения. Спасатели уже вызваны!")

    def to_ride(self, number_floor, i=0):
        if not self.elevator_broken:
            num_break = random.randint(1, 5)
            if num_break == 5:
                self.break_elevator()
                self.restore_elevator()
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
            if num_break <= 4:
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
        else:
            raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                          "приносим свои извинения. Спасатели уже вызваны!")

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

    def break_elevator(self):
        self.elevator_broken = True
        print("Лифт был сломан, пожалуйста подождите...")
        time.sleep(3)

    def restore_elevator(self, i=10):
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
                if random.randint(4, 10) <= 2:
                    print("")
                    print("Лифт восстановлен успешно!\n")
                    self.elevator_broken = False
                else:
                    print("")
                    self.elevator_broken = True
            i -= 1

    def check_elevator_condition(self):
        print("Состояние лифта:\n")
        print(f"Этаж на котором находится лифт: {self.elevator_location}\nОбщий вес лифта: {self.weigth_units}\n"
              f"Количество пассажиров в ожидает: {self.waiting_count_units}\nКоличество пассажиров в "
              f"лифте: {self.count_units}\n")
