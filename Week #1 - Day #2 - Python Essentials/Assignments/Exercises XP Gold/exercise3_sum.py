def sum_pattern(X):
    x1 = str(X)
    x2 = x1 * 2
    x3 = x1 * 3
    x4 = x1 * 4
    total = int(x1) + int(x2) + int(x3) + int(x4)
    return total

num = int(input("Enter a number: "))
print(f"Result: {sum_pattern(num)}")
