from math import isqrt 
def cntDels(x):
	cnt = 0
	if isqrt(x)**2 == x:
		cnt -= 1
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			cnt += 2
	return cnt

toAns = []
maxCnt = 0

for i in range(394480, 394540+1):
	res = cntDels(i)
	if res > maxCnt:
		toAns = [i]
		maxCnt = res
	elif res == maxCnt:
		toAns.append(i)

for x in toAns:
	for i in range(2, x):
		if x % i == 0:
			print(x, x//i)
			break