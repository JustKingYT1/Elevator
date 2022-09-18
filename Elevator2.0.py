import logging


class WeigthIsHuge(Exception):
    pass


class FloorNumberNotFinded(Exception):
    pass


class Elevator:
    def __init__(self, elevator_capacity):
        self.floors_count = 10
        self.floors_units = {i+1: 0 for i in range(self.floors_count)}
        self.units = []
        self.weigth_units = 0
        self.count_units = 0
        self.elevator_location = self.floors_units[1]
        self.elevator_capacity = elevator_capacity

    def add_unit(self, floor, weigth):
        if floor <= self.floors_count:
            if self.weigth_units <= elev.elevator_capacity:
                    self.units.append(weigth)
                    self.floors_units[floor] = self.units
                    self.count_units += 1
                    self.weigth_units += weigth
                    print(f"Зашел человек!\n\nЭтаж на котором человек выйдет: {floor}\nВес: {weigth}\n")

    def delete_unit(self, i=0):
        number = 0
        while i <= self.floors_count:
            for key in self.floors_units.keys():
                if self.elevator_location == key:
                    if number < 1:
                        print("Человек(люди) вышел(вышли)\n")
                        number += 1
                    for j in range(self.count_units):
                        try:
                            self.weigth_units -= self.floors_units[key][j]
                        except:
                            continue
                    self.floors_units[key] = 0
            i += 1

    def up_bottom(self, number_floor):
        if self.weigth_units <= self.elevator_capacity:
            if number_floor <= self.floors_count:
                self.elevator_location = number_floor
                print(f'Мы прибыли на {self.elevator_location} этаж\n')
            else:
                logging.critical("A message of CRITICAL severity")
                raise FloorNumberNotFinded("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logging.warning("A WARNING")
            raise WeigthIsHuge("Вес выше допустимого")

    def to_move(self, number_floor):
        elev.up_bottom(number_floor)
        elev.delete_unit()

    def __str__(self):
        return f"Этаж на котором находится лифт: {self.elevator_location}\nОбщий вес лифта: {self.weigth_units}\n"


class Unit(Elevator):

    def to_move(self, number_floor):
        elev.up_bottom(number_floor)

    def call_elevator(self, unit_location):
        if unit_location <= elev.floors_count:
            self.to_move(unit_location)
        else:
            raise FloorNumberNotFinded("Указанный этаж находится вне диапазона этажей этого дома")


if __name__ == "__main__":
    elev = Elevator(1200)
    human = Unit(elev)
    human.call_elevator(4)
    elev.add_unit(8, 67)
    elev.add_unit(8, 87)
    print(elev)
    elev.to_move(8)
    print(elev)