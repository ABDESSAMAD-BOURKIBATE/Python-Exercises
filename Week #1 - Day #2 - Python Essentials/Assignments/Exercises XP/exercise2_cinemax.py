family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} has to pay ${cost}")
    total += cost

print(f"Total cost: ${total}")


family_input = {}
while True:
    name = input("Enter name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter age for {name}: "))
    family_input[name] = age

total_input = 0
for name, age in family_input.items():
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} has to pay ${cost}")
    total_input += cost

print(f"Total cost for input family: ${total_input}")
