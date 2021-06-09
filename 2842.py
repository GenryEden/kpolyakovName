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

for i in range(int(12034679**0.25)-2, int(23175821**0.25)+2):
	x = i**4
	if 12034679 <= x <= 23175821 and isSimple(i):
		print(x, i**3)