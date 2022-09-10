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
        try:
            for i in range(100):
                print(f"Зашел человек!\n\nЭтаж на котором находится лифт: {self.elevator_location}\nЭтаж на котором человек выйдет: {self.floor_weigth[i][i]}\nВес: {self.floor_weigth[i][i+1]}\nОбщий вес лифта: {self.weigth_units}\n")
        except:
            return None
    def elevator_call(self, calling_char):
        CALLING_CHAR = "Y"
        return calling_char == CALLING_CHAR

    def to_ride(self, number_floor):
        if self.elevator_call:
            if self.weigth_units <= self.elevator_capacity:
                if number_floor < self.floors_count:
                    self.elevator_location = number_floor
                    print(f'Мы прибыли на {number_floor} этаж\n')
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
                    print("Человек вышел!\n")
                i +=1
        except:
            return None


if __name__ == "__main__":
    elev = Elevator(10, 1, 120)
    elev.elevator_call("Y")
    elev.to_ride(3)
    (elev.add_unit([5, 46]))
    elev.to_ride(5)
    elev.delete_unit()
    (elev.add_unit([6, 45]))
    elev.to_ride(6)
    elev.delete_unit()
    (elev.add_unit([3, 55]))
    elev.to_ride(3)
    elev.delete_unit()
