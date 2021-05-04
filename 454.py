def f(x):
	if x < 3:
		return 0
	elif x == 3:
		return 1
	elif x == 15:
		return 0
	else:
		ans = f(x-1)
		if x % 2 == 0:
			if not(x//2 < 10 < x):
				ans += f(x//2)
		return ans

print(f(45))