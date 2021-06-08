from math import isqrt

def isSimple(x):
	for i in range(2, min(x, isqrt(x)+1)):
		if x % i == 0:
			return False
	return True

cnt = 1
for x in range(194493, 196500, 100):
	if isSimple(x):
		print(cnt, x)
		cnt += 1