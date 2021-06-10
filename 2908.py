from math import isqrt
def cntDels(x):
	cnt = 0
	if isqrt(x)**2 == x:
		cnt -= 1
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			cnt += 2
	return cnt

def getBigDel(x):
	for i in range(2, x):
		if x % i == 0:
			return x//i

maximal = 0
minimal = 0 
maxCnt = 0
for i in range(586132, 586430+1):
	res = cntDels(i)
	if res > maxCnt:
		maxCnt = res
		minimal = i
		maximal = i
	elif res == maxCnt:
		maximal = i

print(maxCnt, getBigDel(minimal))
print(maxCnt, getBigDel(maximal))