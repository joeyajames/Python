# Python Dictionary Comprehensions
# (c) Joe James 2023

# 1. math function to compute values using list
dict1 = {x: 2*x for x in [0, 2, 4, 6]}
print ('1. ', dict1)

# 2. math function to compute values using range
dict2 = {x: x**2 for x in range(0, 7, 2)}
print ('2. ', dict2)

# 3. from chars in a string
dict3 = {x: ord(x) for x in 'Kumar'}
print ('3. ', dict3)

# 4. given lists of keys & values
x = ['Aditii', 'Brandon', 'Clumley', 'Magomed', 'Rishi']
y = [1, 2, 3, 13, 18] 
dict4 = {i: j for (i,j) in zip(x,y)} 
print ('4. ', dict4)

# 5. from chars in a string
x = "python"
dict5 = {i: 3*i.upper() for i in x}
print('5. ', dict5)

# 6. list comprehension for the value
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]
dict6 = {i: [i + 2*j for j in y] for i in x}
print('6. ', dict6)

#7. using items
x = {'A':10, 'B':20, 'C':30}
dict7 = {i: j*2 for (i,j) in x.items()}
print('7. ', dict7)

# 8. conditional comprehension
dict8 = {i: i**3 for i in range(10) if i%2 == 0}
print('8. ', dict8)

# 9. if-else conditional comprehension
x = {'A':10, 'B':20, 'C':30}
dict9 = {i: (j if j < 15 else j+100) for (i,j) in x.items()}
print('9. ', dict9)

# 10. transformation from an existing dict
x = {'A':10, 'B':20, 'C':30}
dict10 = {i: x[i]+1 for i in x}
print('10. ', dict10)




