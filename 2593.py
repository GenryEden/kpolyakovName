from functools import cache

def sumOfNumerals(x):
	return sum([int(i) for i in str(x)])

@cache
def getSimpleDels(x):
	if x == 1:
		return {}
	i = 2
	while x % i != 0:
		i += 1
	nums = getSimpleDels(x//i).copy()
	try:
		nums[i] += 1
	except KeyError:
		nums[i] = 1
	return nums

def check(x):
	nums = getSimpleDels(x)
	for num in nums:
		if nums[num] > 1:
			return False
	return True

ans = 0
for x in range(2945, 18294+1):
	if check(x):
		ans += sumOfNumerals(x)

print(ans)