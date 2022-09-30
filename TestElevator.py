import unittest
from Elevator import Elevator
from Human import Human


class TestElevator(unittest.TestCase):
    def setUp(self) -> None:
        self.elev = Elevator(10, 1200)
        self.human = Human()

    def test_move_elevator(self):
        self.assertEqual(self.elev.to_ride(6), 6)
