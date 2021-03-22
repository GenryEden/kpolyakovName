from functools import lru_cache

@lru_cache
def f(x):
	if x <= 0:
		return 0
	elif x == 1:
		return 1
	else:
		ans = f(x-2)
		if x % 3 == 0:
			ans += f(x//3)
		return ans

print(f(49))