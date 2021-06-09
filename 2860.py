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

print(sum([x for x in range(1060, 18813) if isSimple(x)]))