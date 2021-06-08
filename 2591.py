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

print(len([x for x in range(2, 200000+1) if isSimple(x)]))