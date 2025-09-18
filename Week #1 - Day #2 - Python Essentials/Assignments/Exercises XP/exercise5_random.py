import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    print(f"Your number: {user_number}, Random number: {random_number}")
    if user_number == random_number:
        print("Success! Numbers match.")
    else:
        print("Fail! Numbers do not match.")

num = int(input("Enter a number between 1 and 100: "))
compare_numbers(num)