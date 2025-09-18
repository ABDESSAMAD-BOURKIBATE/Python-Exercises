from datetime import datetime

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

candles_count = age % 10

is_leap_year = (birthdate.year % 4 == 0 and (birthdate.year % 100 != 0 or birthdate.year % 400 == 0))

def print_cake(candles):
    candle_line = " " + "i" * candles
    print(f"    ___{candle_line}___")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~\n")

print_cake(candles_count)

if is_leap_year:
    print("🎉 You were born in a leap year! Here's another cake!")
    print_cake(candles_count)
