# Temperature Conversion Program

def menu():
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Enter a choice: ")
    return choice

def to_celsius(f):
    return int((f - 32) / 1.8)

def to_fahrenheit(c):
    return int(c * 1.8 + 32)

def main():
    choice = menu()
    while choice != '3':
        if choice == '1':
            c = float(input("Enter degrees Celsius: "))
            print(f"{c}C = {to_fahrenheit(c)}F")
        elif choice == '2':
            f = float(input("Enter degrees Fahrenheit: "))
            print(f"{f}F = {to_celsius(f)}C")
        else:
            print("Invalid choice.")
        choice = menu()

if __name__ == "__main__":
    main()