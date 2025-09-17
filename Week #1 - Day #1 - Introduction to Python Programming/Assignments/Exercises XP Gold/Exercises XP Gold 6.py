import random

wins = 0
losses = 0

while True:
    user_input = input("Enter a number (1-9) or 'quit' to exit: ")

    if user_input.lower() == "quit":
        print("Games won:", wins)
        print("Games lost:", losses)
        break

    try:
        user_num = int(user_input)
        random_num = random.randint(1, 9)

        if user_num == random_num:
            print("Winner 🎉")
            wins += 1
        else:
            print("Better luck next time. The number was:", random_num)
            losses += 1

    except ValueError:
        print("Please enter a valid number between 1 and 9.")