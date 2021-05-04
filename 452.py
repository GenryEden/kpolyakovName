def f(x):
	if x < 3:
		return 0
	elif x == 3:
		return 1
	elif x == 18:
		return 0
	else:
		ans = f(x-1)
		if not(x-3 < 12 < x):
			ans += f(x-3)
		return ans

print(f(21))