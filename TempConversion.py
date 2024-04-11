def menu():
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Enter a choice: ").strip()  # Added .strip() to remove leading/trailing whitespace
    return choice

def to_celsius(f):
    return (f - 32) / 1.8  # Removed unnecessary conversion to int

def to_fahrenheit(c):
    return c * 1.8 + 32  # Removed unnecessary conversion to int

def main():
    choice = menu()
    while choice != '3':  # Changed 3 to '3' to compare with string
        if choice == '1':
            c = float(input("Enter degrees Celsius: "))  # Changed eval to float for safer input parsing
            fahrenheit = to_fahrenheit(c)
            print(f"{c}C = {fahrenheit}F")  # Using f-strings for cleaner output formatting
        elif choice == '2':
            f = float(input("Enter degrees Fahrenheit: "))  # Changed eval to float for safer input parsing
            celsius = to_celsius(f)
            print(f"{f}F = {celsius}C")  # Using f-strings for cleaner output formatting
        else:
            print("Invalid choice.")
        choice = menu()

if __name__ == "__main__":  # Added guard to ensure main() runs only if the script is executed directly
    main()
