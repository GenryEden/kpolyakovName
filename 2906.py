from math import isqrt

for i in range(isqrt(194441)-1, isqrt(196500)+2):
	x = i**2
	if 194441 <= x <= 196500:
		print(x, i)