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
cnt = 0
for i in range(1371085, 1371134+1):
	if isSimple(i):
		cnt += 1
		print(cnt, i)