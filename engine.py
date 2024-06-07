from typing import List
from dataclasses import dataclass

@dataclass
class Car:
    description: str
    seat_number: int 
    cost: int
    multiplier: int = 1

def find_optimal_config(user_input: int, seat_config: List[Car]) -> Car:
    min = seat_config[0]
    for pair in seat_config:
        multiplier = int(user_input/pair.seat_number) if user_input%pair.seat_number == 0 else int(user_input/pair.seat_number) + 1
        pair.multiplier = multiplier
        if not min:
            min = pair
        if pair.multiplier * pair.cost <  min.multiplier * min.cost:
            min = pair
    return min
