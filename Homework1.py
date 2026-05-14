def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent

def main():
    try:
        # Take user input
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))

        # Calculate power
        result = power(base, exponent)

        # Display result
        print(f"{base} raised to the power {exponent} is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()