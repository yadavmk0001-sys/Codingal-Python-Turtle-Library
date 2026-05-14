# Simple Binary <-> Decimal Converter

def binary_to_decimal(binary_str):
    """Convert binary string to decimal integer."""
    try:
        return int(binary_str, 2)
    except ValueError:
        print("Invalid binary number.")
        return None

def decimal_to_binary(decimal_num):
    """Convert decimal integer to binary string."""
    try:
        decimal_num = int(decimal_num)
        return bin(decimal_num)[2:]  # Remove '0b' prefix
    except ValueError:
        print("Invalid decimal number.")
        return None

# Example usage
choice = input("Enter 'b2d' for Binary to Decimal or 'd2b' for Decimal to Binary: ").strip().lower()

if choice == 'b2d':
    binary_input = input("Enter a binary number: ").strip()
    result = binary_to_decimal(binary_input)
    if result is not None:
        print(f"Decimal value: {result}")

elif choice == 'd2b':
    decimal_input = input("Enter a decimal number: ").strip()
    result = decimal_to_binary(decimal_input)
    if result is not None:
        print(f"Binary value: {result}")

else:
    print("Invalid choice. Please enter 'b2d' or 'd2b'.")
