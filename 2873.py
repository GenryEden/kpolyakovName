from math import isqrt

def sumOfDels(x):
	s = 1
	if isqrt(x)**2 == x:
		s -= isqrt(x)
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			s += i + x//i
	return s

cnt = 0
for i in range(2, 20000+1):
	if sumOfDels(i) > i:
		cnt += 1

print(cnt)