from functools import lru_cache

@lru_cache
def k(m, n):
	if n < 1:
		return 0
	elif n == 1:
		if m == 0:
			return 1
		else:
			return 0
	else:
		ans = k(m-1, n-1)
		if n % 2 == 0:
			ans += k(m-1, n//2)
		if n % 3 == 0:
			ans += k(m-1, n//3)
		return ans

print(k(8, 34))