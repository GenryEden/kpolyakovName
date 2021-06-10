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
for i in range(2943444, 2943529+1):
	if isSimple(i):
		cnt += 1
		print(cnt, i)