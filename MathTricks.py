import random
# Designed By Aniket Gupta
# Random option for calculation and maths tricks python program
random_choice = random.randint(1,50)
random_choice2 = random.randint(51,100)

# Correct option 
correct_choice = random_choice2 - random_choice

# Random options 
a = random.randint(1,100)
b = correct_choice # Correct option 
c = random.randint(1,100)
d = random.randint(1,100)

# List of random option with one correct option
option_list = [a,b,c,d]

# Random question  
print(random_choice2, '-', random_choice)
print('\n')

# To display random option with one correct option
sorted_option = sorted(option_list) # Sorting for more complex combinations
for option in sorted_option:
    print(option)

# Get user input
my_choice = int(input('Answer: '))

# Decision making
if my_choice == correct_choice:
    print('Correct Answer')
    
else:
    print('Wrong answer')
    print('Correct answer is : ', correct_choice)
