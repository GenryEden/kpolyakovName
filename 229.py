def f(n):
	ans = n
	if n < 5:
		ans += f(n + 1)
		ans += f(n + 3)
	return ans

print(f(1))