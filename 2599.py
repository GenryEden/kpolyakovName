from math import isqrt
from functools import cache

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

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(isqrt(x)+1, x), 2):
		if x % i == 0:
			return False
	return True

def check(x):
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			return isSimple(x//i) and x//i != i

cnt = 0
maximal = 0
for x in range(125697, 190234+1):
	if check(x):
		cnt += 1
		maximal = x

print(cnt, maximal)