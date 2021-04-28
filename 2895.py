from math import isqrt

def isSimple(x):
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			return False
	return True


cnt = 0
for x in range(2484292, 2484370):
	if isSimple(x):
		cnt += 1
		print(cnt, x)