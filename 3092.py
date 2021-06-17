from functools import cache

@cache
def f(x):
	if x < 20:
		return 0
	elif x == 20:
		return 1
	else:
		cnt = f(x-2)+f(x-3)+f(x-5)
		return cnt

print(f(35))