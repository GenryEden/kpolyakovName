from math import isqrt

def infoDels(x):
	s = 0
	c = 0
	if isqrt(x)**2 == x:
		s -= isqrt(x)
		c -= 1
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			s += i + x//i
			c += 2
	return c, s

maxS = 0
ansi = 0

for i in range(268220, 270335+1):
	c, s = infoDels(i)
	if c <= 4 and s >= maxS:
		ansi = i
		maxS = s

res = infoDels(ansi)
print(*res[::-1])