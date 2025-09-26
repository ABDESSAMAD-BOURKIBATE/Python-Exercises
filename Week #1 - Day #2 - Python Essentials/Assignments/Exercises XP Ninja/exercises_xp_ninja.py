# Week #1 - Day #2 - Python Essentials
# Exercises XP Ninja - All Exercises Combined

# ================================
# Exercise 1: Cars Analysis
# ================================
print("=== Exercise 1: Cars Analysis ===")
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

print("\n" + "="*50 + "\n")

# ================================
# Exercise 2: Full Name Function
# ================================
print("=== Exercise 2: Full Name Function ===")
def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"{first_name.title()} {last_name.title()}"

# Examples
print(get_full_name("john", "lee", "hooker"))
print(get_full_name("bruce", "lee"))

print("\n" + "="*50 + "\n")

# ================================
# Exercise 3: Morse Code Translator
# ================================
print("=== Exercise 3: Morse Code Translator ===")
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def english_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morse_to_english(code):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(char, '') for char in code.split(' '))

text = "Hello World"
morse = english_to_morse(text)
print(f"English: {text}")
print(f"Morse: {morse}")
print(f"Back to English: {morse_to_english(morse)}")