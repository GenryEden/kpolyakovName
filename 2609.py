from math import isqrt, floor
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

def check(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			return (x//i != i) and ((x//i) % 10 == i % 10) and isSimple(x//i)

s = 0
cnt = 0
for i in range(264871, 322989+1):
	if check(i):
		s += i
		cnt += 1

print(cnt, floor(s/cnt))

