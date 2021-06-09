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

for i in range(isqrt(3661)-1, isqrt(33625)+1):
	x = i**2
	if 3661 <= x <= 33625 and isSimple(i):
		cnt += 1

print(cnt)