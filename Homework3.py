# Simple mirrored right triangle pattern

try:
    n = int(input("Enter number of rows: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        for i in range(1, n + 1):
            # Print spaces first for mirroring
            print(" " * (n - i) + "*" * i)
except ValueError:
    print("Invalid input. Please enter an integer.")
