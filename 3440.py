from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, isqrt(x)+1, 2):
		if x % i == 0:
			return False
	return True

def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

for i in range(33333, 55555+1):
	s = sumOfNumerals(i)
	if s > 35 and isSimple(i):
		print(i, s)