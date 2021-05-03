def f(n):
	ans = n
	if n < 6:
		ans += f(n+2)
		ans += f(n*3)
	return ans

print(f(1))
