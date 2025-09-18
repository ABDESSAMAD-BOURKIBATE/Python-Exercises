birthdays = {
    "Alice": "1990/05/14",
    "Bob": "1988/11/23",
    "Charlie": "1995/07/30",
    "Diana": "2000/01/12",
    "Eve": "1992/09/05"
}

print("Welcome! You can look up the birthdays of the people in the list!")

print("People in the list:", ", ".join(birthdays.keys()))

name = input("Enter a person's name: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")