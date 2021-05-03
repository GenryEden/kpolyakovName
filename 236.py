def f(n):
	ans = 1
	if n > 0:
		ans += 1
		ans += g(n - 1)
	return ans

def g(n):
	ans = 1
	if n > 1:
		ans += f(n-2)
	return ans

print(f(12))