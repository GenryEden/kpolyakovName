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

minS = float('inf')
ansi = 0

for i in range(573213, 575340+1):
	c, s = infoDels(i)
	if c == 4 and s < minS:
		ansi = i
		minS = s

for i in range(2, ansi):
	if ansi % i == 0:
		print(minS, ansi//i)
		break