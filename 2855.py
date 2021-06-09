from math import isqrt
def check(x):
	cnt = [0, 0]
	if isqrt(x)**2 == x:
		cnt[isqrt(x) % 2] -= 1
	for i in range(1, isqrt(x)+1):
		if x % i == 0:
			cnt[i % 2] += 1
			cnt[(x//i) % 2] += 1
	return cnt[0] == cnt[1] >= 70

for i in range(326496, 649632):
	if check(i):
		for x in range(1001, i+1):
			if i % x == 0:
				print(i, x)
				break