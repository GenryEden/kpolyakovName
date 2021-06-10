from math import isqrt

def check(x):
	s = 0
	for i in str(x):
		i = int(i)
		if i >= 3:
			return False
		s += i
	return s % 10 == 0

def cntDels(x):
	cnt = 0
	if isqrt(x)**2 == x:
		cnt -= 1
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			cnt += 2
	return cnt - 2

cnt = 0
for x in range(1000000, 1300000+1):
	if check(x):
		cnt += 1
		if cnt % 10 == 0:
			print(x, cntDels(x))
