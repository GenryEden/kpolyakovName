from math import isqrt
def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(isqrt(x)+1, x), 2):
		if x % i == 0:
			return False
	return True

i = 2
s = 1
cnt = 0
while True:
	if isSimple(i):
		cnt += 1
		s *= i
		if s > 10000000:
			s //= i
			cnt -= 1
			break
	i += 1

print(s, cnt)