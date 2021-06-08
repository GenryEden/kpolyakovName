from functools import cache

@cache
def getSimpleDels(X):
	x = X
	if X == 1:
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

def countDels(x):
	ans = 1
	nums = getSimpleDels(x)
	for num in nums:
		ans *= nums[num] + 1
	return ans - 2

for x in range(1, int(535672891**0.25)+1):
	n = x**4
	if 358633892 <= n <= 535672891 and countDels(n) == 3:
		print(n, x**3)
