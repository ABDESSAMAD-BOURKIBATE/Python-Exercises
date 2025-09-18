cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = [car.strip() for car in cars_str.split(",")]

print(f"There are {len(cars_list)} manufacturers.")

print("Manufacturers in reverse order:", sorted(cars_list, reverse=True))

count_o = sum('o' in car.lower() for car in cars_list)
print(f"Number of manufacturers with 'o': {count_o}")

count_no_i = sum('i' not in car.lower() for car in cars_list)
print(f"Number of manufacturers without 'i': {count_no_i}")

cars_list_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_cars = list(dict.fromkeys(cars_list_with_duplicates))  
print(f"Companies without duplicates ({len(unique_cars)}): {', '.join(unique_cars)}")

reversed_names = [car[::-1] for car in sorted(unique_cars)]
print("Reversed letters in A-Z order:", reversed_names)
