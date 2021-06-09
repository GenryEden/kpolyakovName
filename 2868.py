from math import isqrt
from functools import cache

@cache
def sumDels(x):
	s = 0
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			s += i + x//i
	if isqrt(x)**2 == x:
		s -= isqrt(x)
	return s
cnt = 0
maximal = 0

for x in range(2, 263000):
	if sumDels(sumDels(x)) == x*2:
		cnt += 1
		maximal = x

print(cnt, maximal)