def f(n):
	ans = 1
	if n > 0:
		ans += f(n-2)
		ans += f(n//2)
	return ans

print(f(7))