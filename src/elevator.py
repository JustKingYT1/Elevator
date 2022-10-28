from loguru import logger
import random
import time
from human import Passenger
from saver import SaverToJSON as s
from loader import LoaderToJson as l
from exceptions import Exceptions as ex


# noinspection PyBroadException
class Elevator:
    def __init__(self, floors_count, elevator_capacity):
        parameters = l.load("../docs/parameters.json")
        self.list_unit = []
        self.num_break = 0
        self.floors_count = floors_count
        self.elevator_capacity = elevator_capacity
        self.weigth: int = 0
        self.exit_floor: int = 0
        self.unit_location: int = 0
        self.waiting_units = parameters["waiting_units"]
        self.waiting_count_units = parameters["waiting_count_units"]
        self.units = parameters["units"]
        self.weigth_units = parameters["weigth_units"]
        self.count_units = parameters["count_units"]
        self.elevator_location = parameters["elevator_location"]

    def move(self, number_floor):
        if self.weigth_units <= self.elevator_capacity:
            if self.floors_count >= number_floor > 0:
                self.elevator_location = number_floor
            else:
                logger.critical("A message of CRITICAL severity")
                raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logger.warning("A WARNING")
            raise ex.WeigthCapacityError("Вес выше допустимого")

    def auto_move_for_wait_units(self):
        i = 0
        if self.weigth_units <= self.elevator_capacity:
            if self.elevator_location <= self.floors_count:
                count_waiting_units = self.waiting_count_units
                while i != count_waiting_units:
                    j = 0
                    try:
                        while j < self.floors_count:
                            if self.elevator_location <= self.floors_count:
                                if self.elevator_location < self.waiting_units[0][2]:
                                    self.elevator_location += 1
                                elif self.elevator_location > self.waiting_units[0][2]:
                                    self.elevator_location -= 1
                                elif self.elevator_location == self.waiting_units[0][2]:
                                    break
                            j += 1
                    except:
                        i += 1
                        continue
                    print("")
                    print(f"Мы прибыли на {self.elevator_location} этаж")
                    print("")
                    self.add_units()
                    self.delete_waiting_units()
                    i += 1
                self.save()
            else:
                logger.critical("A message of CRITICAL severity")
                raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logger.warning("A WARNING")
            raise ex.WeigthCapacityError("Вес выше допустимого")

    def auto_move_for_units(self):
        i = 0
        if self.weigth_units <= self.elevator_capacity:
            if self.elevator_location <= self.floors_count:
                count_units = self.count_units
                while i != count_units:
                    j = 0
                    while j < self.floors_count:
                        if self.elevator_location < self.units[0][0]:
                            self.elevator_location += 1
                        elif self.elevator_location > self.units[0][0]:
                            self.elevator_location -= 1
                        elif self.elevator_location == self.units[0][0]:
                            break
                        j += 1
                    print("")
                    print(f"Мы прибыли на {self.elevator_location} этаж")
                    print("")
                    self.delete_units()
                    i += 1
                self.save()
            else:
                logger.critical("A message of CRITICAL severity")
                raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logger.warning("A WARNING")
            raise ex.WeigthCapacityError("Вес выше допустимого")

    def add_waiting_units(self, unit: Passenger):
        if self.unit_location <= self.floors_count:
            self.exit_floor = unit.exit_floor()  # Этаж на котором пассажир выйдет
            self.weigth = unit.unit_weigth()  # Вес багажа и его пассажира
            self.unit_location = unit.unit_location()  # местоположение ожидающего пассажира
            self.waiting_count_units += 1
            self.waiting_units.append([unit.exit_floor(), unit.unit_weigth(), unit.unit_location()])
            self.save()
            print(f"Этаж на котором человек ожидает лифт: {self.unit_location}\nЭтаж на котором человек выйдет: "
                  f"{self.exit_floor}\nВес пассажира и его багажа, если он есть: {self.weigth}кг\n")
        else:
            logger.critical("A message of CRITICAL severity")
            raise ex.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")

    def delete_waiting_units(self):
        i = 0
        try:
            while i < 100:
                if self.elevator_location == self.waiting_units[0][2]:  # сравнение местоположения лифта с
                    # местоположением ожидающего пассажира
                    self.waiting_count_units -= 1
                    self.waiting_units.pop(0)
                    self.save()
                    print("Очередь уменьшилась на 1\n")
                i += 1
        except:
            pass

    def add_units(self):
        i = 0
        while i < self.waiting_count_units:
            if self.weigth_units <= self.elevator_capacity:
                if self.weigth_units <= self.elevator_capacity:
                    if self.elevator_location == self.waiting_units[i][2]:  # Сравнение местоположения пассажира с
                        # этажом, на котором он находится
                        self.weigth_units += self.waiting_units[i][1]  # Вес пассажира и его багажа
                        self.count_units += 1
                        self.units.append(self.waiting_units[i])  # Добавление пассажира в список
                        # пассажиров находящихся в лифте
                        self.save()
                        print("Человек зашел!\n")
                    i += 1
            else:
                logger.warning("A WARNING")
                raise ex.WeigthCapacityError("Вес выше допустимого")

    def delete_units(self):
        i = 0
        while i < self.count_units:
            if self.elevator_location == self.units[i][0]:  # Сравнение местоположения пассажира с
                # этажом, на котором он выйдет
                self.count_units -= 1
                self.weigth_units -= self.units[i][1]  # Вес пассажира и его багажа
                self.units.pop(i)
                self.save()
                print("Человек вышел!\n")
            i += 1

    def to_ride(self, number_floor):
        self.break_elevator()
        self.move(number_floor)
        print(f'Мы прибыли на {number_floor} этаж\n')
        self.add_units()
        self.delete_waiting_units()
        self.delete_units()
        self.save()
        return number_floor

    def check_waiting_units(self):
        i = 0
        self.save()
        try:
            while i < self.waiting_count_units + 100:
                print(f"{i + 1}:\nЭтаж на котором человек ожидает лифт: {self.waiting_units[i][2]}\nЭтаж куда едет "
                      f"пассажир: {self.waiting_units[i][0]}\nВес пассажира и его багажа,"
                      f" если он есть: {self.waiting_units[i][1]}кг\n")
                i += 1
        except:
            pass

    def check_units(self):
        i = 0
        self.save()
        try:
            while i < self.count_units + 100:
                print(
                    f"{i + 1}:\nЭтаж куда едет пассажир: {self.units[i][0]}\nВес пассажира и его багажа, если он есть:"
                    f" {self.units[i][1]}кг\n")
                i += 1
        except:
            pass

    def break_elevator(self):
        num_break = random.randint(1, 5)
        if num_break == 5:
            print("Лифт был сломан, пожалуйста подождите...")
            time.sleep(3)
            self.restore_elevator()

    @staticmethod
    def restore_elevator():
        i = 10
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
                if random.randint(1, 10) <= 5:
                    print("")
                    print("Лифт восстановлен успешно!\n")
                else:
                    logger.critical("A message of CRITICAL severity")
                    raise ex.RestoreElevatorError("Не удалось восстановить лифт, "
                                                  "приносим свои извинения. Спасатели уже вызваны!")
            i -= 1

    def save(self):
        to_save = {
            "units": self.units,
            "weigth_units": self.weigth_units,
            "count_units": self.count_units,
            "waiting_units": self.waiting_units,
            "waiting_count_units": self.waiting_count_units,
            "elevator_location": self.elevator_location
        }
        s.save("../docs/parameters.json", to_save)

    def check_elevator_condition(self):
        self.save()
        print("Состояние лифта:\n")
        print(f"Этаж на котором находится лифт: {self.elevator_location}\nОбщий вес лифта: {self.weigth_units}\n"
              f"Количество пассажиров в ожидает: {self.waiting_count_units}\nКоличество пассажиров в "
              f"лифте: {self.count_units}\n")
