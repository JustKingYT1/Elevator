ex = Exception("Вес выше ожидаемого")
ex1 = Exception("Номер этажа не соответствует количеству этажей")


class Elevator:
    def __init__(self, floors_count, elevator_location, elevator_capacity):
        self.floors_count = floors_count
        self.elevator_location = elevator_location
        self.elevator_capacity = elevator_capacity
        self.floor_weigth = []
        self.weigth_units = 0

    def add_unit(self, floor_weigth: list):
        self.floor_weigth.append(floor_weigth)
        self.weigth_units += floor_weigth[1]

    def elevator_call(self, calling_char):
        CALLING_CHAR = "Y"
        return calling_char == CALLING_CHAR

    def to_ride(self, number_floor):
        if self.elevator_call:
            if self.weigth_units <= self.elevator_capacity:
                if number_floor < self.floors_count:
                    self.elevator_location = number_floor
                else:
                    raise ex1
            else:
                raise ex

    def delete_unit(self, i=0):
        try:
            while i < 10:
                if self.elevator_location == self.floor_weigth[i][i]:
                    self.weigth_units -= self.floor_weigth[i][i+1]
                    self.floor_weigth.pop(i)
                i +=1
        except:
            return None

    def __str__(self):
        return f"Этаж на котором находится лифт: {self.elevator_location}\nЭтаж на котором человек выйдет, вес: {self.floor_weigth}\nОбщий вес лифта: {self.weigth_units}\n"


if __name__ == "__main__":
    elev = Elevator(10, 1, 120)
    elev.elevator_call("Y")
    elev.to_ride(3)
    elev.add_unit([3, 45])
    print(elev)
    elev.delete_unit()
    elev.add_unit([4, 55])
    print(elev)
    elev.to_ride(4)
    elev.delete_unit()
    print(elev)
