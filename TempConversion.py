# Temperature Conversion Program

def menu():
	print("\n1. Celsius to Fahrenheit")
	print("2. Fahrenheit to Celsius")
	print("3. Exit")
	choice = input("Enter a choice: ")
	return choice
	
def to_celsius(fahrenheit):
	return (fahrenheit - 32) / 1.8

def to_fahrenheit(celsius):
	return celsius * 1.8 + 32
	
def main():
	choice = menu()
	while choice != '3':
		if choice == '1':
			celsius = float(input("Enter degrees Celsius: "))
			print(f"{celsius}C = {to_fahrenheit(celsius)}F")
		elif choice == '2':
			fahrenheit = float(input("Enter degrees Fahrenheit: "))
			print(f"{fahrenheit}F = {to_celsius(fahrenheit)}C")
		else:
			print("Invalid choice.")
		choice = menu()
		
if __name__ == "__main__":	
	main()