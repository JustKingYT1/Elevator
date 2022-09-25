import unittest
from Elevator import Elevator, Unit


class TestElevator(unittest.TestCase):
    def setUp(self) -> None:
        self.elev = Elevator(10, 1200)
        self.human = Unit

    def test_move_elevator(self):
        self.assertEqual(self.elev.to_ride(6), 6)
