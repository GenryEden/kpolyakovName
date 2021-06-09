from math import isqrt

def check(x):
	if x % 2 == 0:
		return False
	cnt = 0
	if isqrt(x)**2 == x:
		cnt -= 1
	for i in range(3, isqrt(x)+1):
		if x % i == 0:
			cnt += 2
	return cnt > 70

for i in range(321654+1, 654321+1, 2):
	if check(i):
		for k in range(3, isqrt(i)+1, 2):
			if i % k == 0:
				print(i, i//k)
				break
	# print(i)