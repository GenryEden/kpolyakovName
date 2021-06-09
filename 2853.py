from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(isqrt(x)+2, x), 2):
		if x % i == 0:
			return False
	return True

def check(x):
	for i in range(2, min(isqrt(x)+2, x)):
		if x % i == 0:
			if x//i != i and isSimple(x//i):
				return x//i, i
			else:
				return False
	return False

minDist = float('inf')
ans = [0, 0]
for i in range(309829, 365874+1):
	res = check(i)
	if res and minDist > res[0] - res[1]:
		minDist = res[0] - res[1]
		ans = res
print(*sorted(ans))
