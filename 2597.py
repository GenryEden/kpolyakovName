from math import isqrt

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

def sumOfNumerals(x):
	return sum([int(i) for i in str(x)])

ans = 0

for x in range(3159, 31584):
	if isSimple(x):
		ans += sumOfNumerals(x)

print(ans)