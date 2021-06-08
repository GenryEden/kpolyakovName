from math import isqrt
def isSimple(x):
	for i in range(2, min(isqrt(x)+2, x)):
		if x % i == 0:
			return False
	return True

cnt = 0
for x in range(4301614, 4301717+1):
	if isSimple(x):
		cnt += 1
		print(cnt, x)
