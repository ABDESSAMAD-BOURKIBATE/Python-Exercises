import random

class Game:
    def get_user_item(self):
        """Ask the user to select rock/paper/scissors, with validation."""
        choices = ["rock", "paper", "scissors"]
        user_input = None
        while user_input not in choices:
            user_input = input("Select (rock, paper, scissors): ").lower()
            if user_input not in choices:
                print("❌ Invalid choice, please try again.")
        return user_input

    def get_computer_item(self):
        """Randomly select rock/paper/scissors for the computer."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Determine game result: win, loss, or draw."""
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"

    def play(self):
        """Play one round of Rock-Paper-Scissors."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            print(f"✅ You selected {user_item}. Computer selected {computer_item}. You WIN! 🎉")
        elif result == "loss":
            print(f"❌ You selected {user_item}. Computer selected {computer_item}. You LOSE.")
        else:
            print(f"🤝 You selected {user_item}. Computer selected {computer_item}. It's a DRAW.")

        return result
