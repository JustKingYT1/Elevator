import logging


class NumberFloorError(Exception):
    pass


class WeigthCapacityError(Exception):
    pass


class Elevator:
    def __init__(self, floors_count, elevator_capacity):
        self.floors_count = floors_count
        self.elevator_location = 1
        self.elevator_capacity = elevator_capacity

    def move(self, number_floor):
        if human.weigth_units <= self.elevator_capacity:
            if number_floor <= self.floors_count:
                self.elevator_location = number_floor
                print(f'Мы прибыли на {number_floor} этаж\n')
            else:
                logging.critical("A messageтеп of CRITICAL severity")
                raise NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logging.warning("A WARNING")
            raise WeigthCapacityError("Вес выше допустимого")

    def to_ride(self, number_floor):
        elev.move(number_floor)
        try:
            for i in range(human.count_units):
                try:
                    human.delete_unit()
                except:
                    pass
        except:
            pass

    def __str__(self):
        return f"Этаж на котором находился лифт: {self.elevator_location}\nОбщий вес лифта: {human.weigth_units}\nКоличество пассажиров в лифте: {human.count_units}\n"


class Unit:

    def __init__(self):
        self.units = []
        self.weigth_units = 0
        self.count_units = 0

    def call_elevator(self, unit_location):
        elev.move(unit_location)

    def add_unit(self, unit: list):
        floor = unit[0]
        weigth = unit[1]
        self.units.append(unit)
        self.weigth_units += weigth
        self.count_units += 1
        print(f"Зашел человек!\n\nЭтаж на котором человек выйдет: {floor}\nВес: {weigth}\n")

    def delete_unit(self, i=0):
        while i <= self.count_units:
            if elev.elevator_location == self.units[i][0]:
                self.count_units -= 1
                self.weigth_units -= self.units[i][1]
                self.units.pop(i)
                print("Человек вышел!\n")
            i += 1

    def __str__(self):
        print("Все пассажиры в лифте на данный момент:")
        for i in range(human.count_units):
            print(f"{i + 1})\nЭтаж на котором человек выйдет: {self.units[i][0]}\nВес: {self.units[i][1]}")
        return ""


if __name__ == "__main__":
    elev = Elevator(10, 1200)
    human = Unit()
    while True:
        num_elev_location = elev.elevator_location
        print("1 - Вызов лифта\n2 - Передвижение лифта\n3 - Информация о лифте\n4 - Выключение лифта\n")
        number = int(input("Введите число соответствующее команде лифта -> "))
        print("")
        if number == 1:
            num = int(input("Введите номер этажа куда вызывается лифт -> "))
            print("")
            human.call_elevator(num)
            print("1 - Добавление пассажира\n2 - Отмена операции\n")
            num1 = int(input("Введите число соответствующее команде лифта -> "))
            print("")
            if num1 == 1:
                floor = int(input("Введите этаж, на который поедет пассажир -> "))
                weigth = int(input("Введите вес пассажира и его багажа -> "))
                print("")
                human.add_unit([floor, weigth])
            elif num1 == 2:
                elev.to_ride(num_elev_location)
                continue
        elif number == 2:
            num_floor = int(input("Введите номер этажа куда поедет лифт -> "))
            print("")
            elev.to_ride(num_floor)
        elif number == 3:
            print(elev)
            print(human)
        elif number == 4:
            break
        else:
            print("Неверно введен номер команды, повторите попытку\n")
