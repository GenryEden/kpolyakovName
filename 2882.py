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

cnt = 0
maximal = 0
for i in range(int(904528**0.25)-2, int(997438**0.25)+2):
	x = i**4
	if 904528 <= x <= 997438 and isSimple(i):
		cnt += 1
		maximal = x

print(cnt, maximal)