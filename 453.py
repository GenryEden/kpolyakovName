def f(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	elif x == 10:
		return 0
	else:
		ans = f(x-1)
		if not(x-5 < 15 < x):
			ans += f(x-5)
		return ans

print(f(26))