def f(x):
	if x < 4:
		return 0
	elif x == 4:
		return 1
	elif x == 12:
		return 0
	else:
		ans = f(x-1)
		if x % 3 == 0:
			if not(x//3 < 6 < x):
				ans += f(x//3)
		return ans

print(f(50))