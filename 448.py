def f(x):
	if x < 1:
		return 0
	elif x == 1:
		return 1
	else:
		ans = f(x-1)
		if x - 1 != 7:
			ans += f(x-2)
		return ans

print(f(12))