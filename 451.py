def f(x):
	if x < 5:
		return 0
	elif x == 5:
		return 1
	elif x == 12:
		return 0
	else:
		ans = f(x-1)
		if not(x-3 < 15 < x):
			ans += f(x-3)
		return ans

print(f(25))