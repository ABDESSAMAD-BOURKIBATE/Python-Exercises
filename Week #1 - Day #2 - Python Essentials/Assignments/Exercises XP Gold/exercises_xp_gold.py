# Week #1 - Day #2 - Python Essentials
# Exercises XP Gold - All Exercises Combined

import random

# ================================
# Exercise 1: Birthday Lookup
# ================================
print("=== Exercise 1: Birthday Lookup ===")
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
    print(f"Sorry, we don't have the birthday information for {name}.")

print("\n" + "="*50 + "\n")

# ================================
# Exercise 3: Sum Pattern
# ================================
print("=== Exercise 3: Sum Pattern ===")
def sum_pattern(X):
    x1 = str(X)
    x2 = x1 * 2
    x3 = x1 * 3
    x4 = x1 * 4
    total = int(x1) + int(x2) + int(x3) + int(x4)
    return total

num = int(input("Enter a number: "))
print(f"Result: {sum_pattern(num)}")

print("\n" + "="*50 + "\n")

# ================================
# Exercise 4: Double Dice
# ================================
print("=== Exercise 4: Double Dice ===")
def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        d1 = throw_dice()
        d2 = throw_dice()
        count += 1
        if d1 == d2:
            break
    return count

def main():
    results = []
    for _ in range(100):
        results.append(throw_until_doubles())
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()