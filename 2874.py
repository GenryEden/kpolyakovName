from math import isqrt
def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+1), 2):
		if x % i == 0:
			return False
	return True

s = 1
i = 2
cnt = 0
while True:
	if isSimple(i):
		s *= i
		cnt += 1
		if s > 20000:
			cnt -= 1
			s //= i
			break
	i += 1
print(s, cnt)