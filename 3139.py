from functools import lru_cache

@lru_cache
def f(n):
	if n < 10:
		return n
	else:
		m = f(n//10)
		d = m%10
		if m < d:
			return d
		else:
			return m

for x in range(999, 99, -1):
	res = f(x)
	if res > 7:
		break

print(x, res)