from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+1), 2):
		if x % i == 0:
			return False
	return True

def check(x):
	for i in range(2, min(x, isqrt(x)+1)):
		if x % i == 0:
			if isSimple(x//i) and x//i != i:
				return x//i - i
			else:
				return False
ans = 0
maxDist = 0
for x in range(631632, 684934+1):
	res = check(x)
	if res and res > maxDist:
		maxDist = res
		ans = x

for i in range(2, ans):
	if ans % i == 0:
		print(i, ans//i)
		break