from functools import cache

@cache
def f(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	else:
		cnt = f(x-1)
		if x % 3 == 0:
			cnt += f(x*2//3)
		return cnt

print(f(22))