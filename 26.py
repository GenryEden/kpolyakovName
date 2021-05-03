def f(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	elif x == 25:
		return 0
	else:
		ans = 0
		ans += f(x-1)
		if x % 2 == 0 and not(x//2 < 14 < x):
			ans += f(x//2)
		return ans

print(f(29))