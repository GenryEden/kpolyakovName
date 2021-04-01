def f(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	else:
		ans = f(x-1) + f(x-3)
		if int(x**0.5) == x**0.5:
			ans += f(int(x**0.5))
		return ans

print(f(19))