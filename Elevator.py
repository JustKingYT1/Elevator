import logging


class TypeUniversalException(Exception):
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
                logging.critical("A message of CRITICAL severity")
                raise TypeUniversalException("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            logging.warning("A WARNING")
            raise TypeUniversalException("Вес выше допустимого")

    def __str__(self):
        return f"Этаж на котором находится лифт: {self.elevator_location}\nОбщий вес лифта: {human.weigth_units}\nКоличество людей в лифте: {human.count_units}\n"


class Unit:

    def __init__(self):
        self.units = []
        self.weigth_units = 0
        self.count_units = 0

    def add_unit(self, unit: list):
        self.units.append(unit)
        self.weigth_units += unit[1]
        self.count_units += 1
        print(f"Зашел человек!\n\nЭтаж на котором человек выйдет: {unit[0]}\nВес: {unit[1]}\n")

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

    def delete_unit(self, i=0):
        while i <= self.count_units:
            if elev.elevator_location == self.units[i][0]:
                self.count_units -= 1
                self.weigth_units -= self.units[i][1]
                self.units.pop(i)
                print("Человек вышел!\n")
            i += 1

    #def __str__(self):
     #   print("Все пассажиры в лифте на данный момент:")
    #    for i in range(human.count_units):
    #        print(f"{i + 1})\nЭтаж на котором человек выйдет: {self.units[i][0]}\nВес: {self.units[i][1]}")
    #    return ""


if __name__ == "__main__":
    elev = Elevator(10, 1200)
    human = Unit()
    human.to_ride(3)
    human.add_unit([5, 78])
    human.add_unit([2, 65])
    human.add_unit([5, 34])
    print(elev)
    human.to_ride(5)
    print(elev)
    human.to_ride(2)
    print(elev)