from functools import reduce

domain = [1, 2, 3, 4, 5]

# Higher Order Function
# Functions that take input or output back functions
output_range = map(lambda x: x * 2, domain)
print(list(output_range))

evens = filter(lambda x: x % 2 == 0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Some', 'thing', 'to', 'compare']
print(sorted(words))

print(sorted(words, key=lambda ele: ele.lower()))

print(sorted(words, key=lambda ele: ele.lower(), reverse=True))

words.sort(key=str.lower)
print(words)
