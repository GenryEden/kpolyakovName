def f(x):
	if x < 1:
		return 0
	elif x == 1:
		return 1
	else:
		ans = f(x-1)
		if x % 2 == 0:
			if not(x//2 < 10 < x):
				ans += f(x//2)
		return ans

print(f(21))