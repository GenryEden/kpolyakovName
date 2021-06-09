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

cnt = 1
for i in reversed(range(1532040, 1532160+1)):
	if isSimple(i):
		print(cnt, i)
		cnt += 1