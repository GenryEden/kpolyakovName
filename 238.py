def f(n):
	if n > 0:
		return g(n - 1)
	return 0

def g(n):
	ans = 1
	if n > 1:
		ans += 1
		ans += f(n - 2)
	return ans

print(f(13))