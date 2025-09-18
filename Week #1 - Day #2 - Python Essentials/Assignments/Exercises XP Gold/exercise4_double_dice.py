import random

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
