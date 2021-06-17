from math import isqrt
def isSimple(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, isqrt(n)+1, 2):
		if n % i == 0:
			return False
	return True

def check(n):
	return isSimple(n) and int(str(n)[0]) > int(str(n)[-1])

maximal21 = 0
cnt = 0
for i in range(2095, 19402+1):
	if check(i):
		cnt += 1
		if i % 100 == 21:
			maximal21 = i

print(cnt, maximal21)