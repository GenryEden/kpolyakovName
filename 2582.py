from math import isqrt

def isSimple(x):
	for i in range(2, min(x, isqrt(x)+1)):
		if x % i == 0:
			return False
	return True

cnt = 0
for x in range(2532421, 2532491+1):
	if isSimple(x):
		cnt += 1
		print(cnt, x)