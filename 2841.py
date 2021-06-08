from functools import cache

@cache
def getSimpleDels(x):
	i = 2
	if x == 1:
		return {}
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

for i in range(1, int(152673836**0.25)+10):
	x = i**4		
	if 106732567 <= x <= 152673836 and countDels(x) == 3:
		print(x, i**3)