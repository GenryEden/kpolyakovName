from functools import lru_cache

@lru_cache
def f(x):
	if x < 1:
		return 0
	if x == 1:
		return 1
	ans = f(x - 1)
	ans += f(x - 3)
	if x % 4 == 0:
		ans += f(x//4)
	return ans

print(f(18))