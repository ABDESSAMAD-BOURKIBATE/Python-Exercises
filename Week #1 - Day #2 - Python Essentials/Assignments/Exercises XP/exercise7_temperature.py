import random

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
        advice = "Brrr, that’s freezing! Wear some extra layers today."
    elif 0 <= temp <= 16:
        advice = "Quite chilly! Don’t forget your coat."
    elif 16 < temp <= 23:
        advice = "Mild weather, dress comfortably."
    elif 24 <= temp <= 32:
        advice = "Warm weather, enjoy your day!"
    else:
        advice = "It’s hot! Stay hydrated."

    print(advice)

main()
