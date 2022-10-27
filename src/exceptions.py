class Exceptions:
    class RestoreElevatorError(Exception):
        def __init__(self, text):
            self.text = text

    class NumberFloorError(Exception):
        def __init__(self, text):
            self.text = text

    class WeigthCapacityError(Exception):
        def __init__(self, text):
            self.text = text
