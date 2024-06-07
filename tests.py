from unittest import TestCase
from engine import Car, find_optimal_config

class TestMain(TestCase):
    def test_find_optimal_config(self):
        user_input = 20
        seat_config = [Car("S", 5, 5000),Car("M", 10, 8000),Car("L", 15, 12000)]
        optimal_config = find_optimal_config(user_input, seat_config)
        self.assertEqual(optimal_config, Car("M", 10, 8000, 2)) 
        
        user_input = 30
        seat_config = [Car("S", 5, 5000),Car("M", 10, 8000),Car("L", 15, 12000)]
        optimal_config = find_optimal_config(user_input, seat_config)
        self.assertEqual(optimal_config, Car("M", 10, 8000, 3))

        user_input = 20
        seat_config = [Car("S", 5, 5000),Car("M", 9, 8000),Car("L", 15, 11000)]
        optimal_config = find_optimal_config(user_input, seat_config)
        self.assertEqual(optimal_config, Car("S", 5, 5000 ,4))
        
        user_input = 30
        seat_config = [Car("S", 5, 5000),Car("M", 9, 8000),Car("L", 15, 11000)]
        optimal_config = find_optimal_config(user_input, seat_config)
        self.assertEqual(optimal_config, Car("L", 15, 11000, 2)) 
