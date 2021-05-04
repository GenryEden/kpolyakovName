def f(x):
	if x < 1:
		return 0
	elif x == 1:
		return 1
	elif x == 6:
		return 0
	else:
		ans = 0
		if not(x-2 < 25 < x):
			ans += f(x-2)
		if x % 3 == 0:
			if not(x//3 < 25 < x):
				ans += f(x//3)
		return ans

print(f(63))