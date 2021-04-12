def f(x):
	if x < 5:
		return 0
	if x == 5:
		return 1
	if x == 10 or x == 15:
		return 0
	ans = f(x-1)
	if x - 1 != 11:
		ans += f(x-2)
		if x - 2 != 11:
			ans += f(x-3)
	return ans 

print(f(18))