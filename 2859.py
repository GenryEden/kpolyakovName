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



for x in range(int(81234**0.25)-2, int(134689**0.25)+2):
	i = x**4
	if isSimple(x) and 81234 <= i <= 134689:
		print(x, x**3)