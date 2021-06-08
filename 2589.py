from functools import cache

@cache
def sumOfDels(x):
	s = 0
	for i in range(1, x):
		if x % i == 0:
			s += i
	return s

for x in range(2, 30000):
	s = sumOfDels(x)
	if s > x and sumOfDels(s) == x:
		print(x, s)
