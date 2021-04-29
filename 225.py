def f(n):
	if n < 3:
		return 1
	else:
		ans = f(n-1)
		ans += f(n-2)
		ans += f(n-2)
		return ans

print(f(6))