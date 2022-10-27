import unittest
from elevator import Elevator
from human import Passenger


class TestElevator(unittest.TestCase):
    def setUp(self) -> None:
        self.elev = Elevator(10, 1200)
        self.passenger = Passenger(65, 4, 10)

    def test_move_elevator(self):
        self.assertEqual(self.elev.to_ride(6), 6)


if __name__ == "__main__":
    unittest.main()
