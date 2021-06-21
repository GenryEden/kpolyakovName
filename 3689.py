from math import isqrt

def isPrime(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, isqrt(x)+1, 2):
		if x % i == 0:
			return False
	return True

def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

s = 0

for x in range(2, 10+1):
	res = toCountSystem(437, x)
	if isPrime(sum([int(i) for i in res])):
		s += x

print(s)