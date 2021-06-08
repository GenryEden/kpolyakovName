from math import isqrt

def cntDels(x):
	cnt = 0
	for i in range(2, x):
		if x % i == 0:
			cnt += 1
	return cnt

def sumOfNumerals(x):
	return sum([int(i) for i in str(x)])

cnt = 0
s = 0

for i in range(isqrt(4099)-1, isqrt(26985)+2):
	x = i**2
	if 4099 <= x <= 26985 and cntDels(x) == 1:
		cnt += 1
		s += sumOfNumerals(x)

print(cnt, s)