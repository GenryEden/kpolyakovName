from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+2), 2):
		if x % i == 0:
			return False
	return True

for i in range(int(152346**0.25)-2, int(957812**0.25)+2):
	x = i**4
	if 152346 <= x <= 957812 and isSimple(i):
		print(x, i**3)