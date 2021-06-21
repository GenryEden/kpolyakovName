from functools import cache

@cache
def f(x):
	if x < 1:
		return 0
	if x == 1:
		return 1
	else:
		cnt = f(x-1)
		if not(x-3 < 4 < x) and not(x-3 < 9 < x):
			cnt += f(x-3)
		if x % 2 == 0 and not(x//2 < 4 < x) and not(x//2 < 9 < x):
			cnt += f(x//2)
		return cnt

print(f(13))