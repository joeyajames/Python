# Program to simply demonstrate If-else in Python Programming
# Program to find wheather the given number is odd or even

#Take input from the user (asking for a number)
user_number = input(int("Enter the number: "))

#Show the number number, user entered
print(f"\nYou have entered: {user_number}")

#Check whethere the number is divisible by 2 and print result

if(user_number % 2 == 0):
  print("You have entered an even number")
  
else:
  print("You have entered an odd number")
