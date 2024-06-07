from engine import Car, find_optimal_config

seat_config = [
        Car("S",5, 5000), # S
        Car("M",9,8000), # M
        Car("L",15,11000) # L
        ]

user_input = input("Please input number (seat): ") 
optimal_config = find_optimal_config(int(user_input), seat_config)
print(f"{optimal_config.description} * {optimal_config.multiplier}") 
print(f"Total = Php {optimal_config.multiplier * optimal_config.cost}")
