# Week #1 - Day #2 - Python Essentials
# Exercises XP - All Exercises Combined

# ================================
# Exercise 1: Lists to Dictionary
# ================================
print("=== Exercise 1: Lists to Dictionary ===")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

print("\n" + "="*50 + "\n")

# ================================
# Exercise 2: Cinemax - Movie Tickets
# ================================
print("=== Exercise 2: Cinemax - Movie Tickets ===")
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

# Bonus - user input version
print("\n--- Bonus: Input your own family ---")
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

print("\n" + "="*50 + "\n")

# ================================
# Exercise 3: Zara Brand Dictionary
# ================================
print("=== Exercise 3: Zara Brand Dictionary ===")
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}

# Change number of stores to 2
brand["number_stores"] = 2

# Print Zara's clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}")

# Add country of creation
brand["country_creation"] = "Spain"

# Add Desigual to competitors if the key exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete creation_date
brand.pop("creation_date", None)

# Print last competitor
print(brand["international_competitors"][-1])

# Print major colors in US
print(brand["major_color"]["US"])

# Print number of key-value pairs
print(len(brand))

# Print all keys
print(list(brand.keys()))

# Update with more_on_zara
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)

# Print number of stores
print(brand["number_stores"])

print("\n" + "="*50 + "\n")

# ================================
# Exercise 4: Geography Function
# ================================
print("=== Exercise 4: Geography Function ===")
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik")
describe_city("Paris", "France")

print("\n" + "="*50 + "\n")

# ================================
# Exercise 5: Random Number Comparison
# ================================
print("=== Exercise 5: Random Number Comparison ===")
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

print("\n" + "="*50 + "\n")

# ================================
# Exercise 6: Shirt Customization
# ================================
print("=== Exercise 6: Shirt Customization ===")
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

# Call function with default values
make_shirt()

# Call function with default text, custom size
make_shirt("Medium")

# Call function with custom size and text
make_shirt("Small", "Python is awesome")

# Call function with keyword arguments
make_shirt(text="Custom Text", size="XL")

print("\n" + "="*50 + "\n")

# ================================
# Exercise 7: Temperature Advice
# ================================
print("=== Exercise 7: Temperature Advice ===")
def get_random_temp(season=None):
    if season == "winter":
        low, high = -10, 16
    elif season == "spring":
        low, high = 0, 23
    elif season == "summer":
        low, high = 16, 40
    elif season in ["autumn", "fall"]:
        low, high = 0, 25
    else:
        low, high = -10, 40
    return round(random.uniform(low, high), 1)

def main():
    season = input("Enter the season (winter, spring, summer, autumn/fall): ").lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp}°C.")

    if temp < 0:
        advice = "Brrr, that's freezing! Wear some extra layers today."
    elif 0 <= temp <= 16:
        advice = "Quite chilly! Don't forget your coat."
    elif 16 < temp <= 23:
        advice = "Mild weather, dress comfortably."
    elif 24 <= temp <= 32:
        advice = "Warm weather, enjoy your day!"
    else:
        advice = "It's hot! Stay hydrated."

    print(advice)

main()

print("\n" + "="*50 + "\n")

# ================================
# Exercise 8: Star Wars Quiz
# ================================
print("=== Exercise 8: Star Wars Quiz ===")
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def run_quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        ans = input(item["question"] + " ").strip()
        if ans.lower() == item["answer"].lower():
            correct += 1
        else:
            incorrect += 1
            wrong_answers.append({"question": item["question"], "your_answer": ans, "correct_answer": item["answer"]})

    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if wrong_answers:
        print("Review your mistakes:")
        for wrong in wrong_answers:
            print(f"Q: {wrong['question']}")
            print(f"Your answer: {wrong['your_answer']}")
            print(f"Correct answer: {wrong['correct_answer']}\n")

    if incorrect > 3:
        print("You had more than 3 wrong answers. Try again!")

run_quiz()