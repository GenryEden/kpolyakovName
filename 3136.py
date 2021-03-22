from functools import lru_cache

@lru_cache
def f(n):
	ans = n - 5
	if n > 1:
		ans += n + 8
		ans += f(n - 2)
		ans += f(n - 3)
	return ans

for x in range(1, 1<<20):
	res = f(x)
	if res > 3200000:
		break

print(x, f(x))