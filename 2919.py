from math import isqrt
def cntDels(x):
	cnt = 0
	if isqrt(x)**2 == x:
		cnt -= 1
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			cnt += 2
	return cnt

for x in range(177399, 177453+1):
	if cntDels(x) == 6:
		for i in range(2, x):
			if x % i == 0:
				print(x//i, x)
				break