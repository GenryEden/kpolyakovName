from math import isqrt
def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+1), 2):
		if x % i == 0:
			return False
	return True

cnt = -1
for i in range(2532000, 2532160+1):
	if isSimple(i):
		cnt += 1
		if cnt % 3 == 0:
			print(cnt+1, i)