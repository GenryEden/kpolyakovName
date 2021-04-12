def f(x):
	if x < 3:
		return 0
	if x == 3:
		return 1
	ans = 0
	if x % 3 != 0:
		ans += f(x - (x % 3))
	ans += f(x - 2)
	return ans

print(f(2*9 + 1*3 + 2))