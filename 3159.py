from math import isqrt

def get(x):
	cnt = 0
	ans = 0
	for a in range(1, isqrt(x)+1):
		if x % a == 0:
			b = x//a
			if b - a <= 90:
				if ans == 0:
					ans = b
				cnt += 1
				if cnt >= 3:
					return ans
	return False


for i in range(500000, 1000000+1):
	res = get(i)
	if res:
		print(i, res)