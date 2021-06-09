from math import isqrt

def f(x):
	cnt = 0
	s = 0
	if isqrt(x)**2 == x:
		cnt -= 1
		s -= isqrt(x)
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			cnt += 2
			s += i + x//i
	return cnt, s

for i in range(135790, 163228+1):
	res = f(i)
	if res[1] > 460000:
		print(*res)