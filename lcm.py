# computes Lowest Common Multiple (LCM) / Least Common Denominator (LCD)
# useful for adding and subtracting fractions

# 2 numbers
def lcm(num1, num2):
	if num1 > num2:
		num1, num2 = num2, num1
	for x in range (num2, num1 * num2 + 1, num2):
		if x % num1 == 0:
			return x

# list of 3 numbers
def lcm3(nums):
	nums.sort()
	worst = nums[0]*nums[1]*nums[2]

	for x in range(nums[2], worst + 1, nums[2]):
		if x % nums[0] == 0 and x % nums[1] == 0:
			return x

print(str(lcm(7, 12)))

nums = [3, 2, 16]
print(str(lcm3(nums)))
