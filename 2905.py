from math import isqrt

for i in range(isqrt(248015)-1, isqrt(251575)+2):
	x = i**2
	if 248015 <= x <= 251575 and x % 2 != 0:
		print(x, i)