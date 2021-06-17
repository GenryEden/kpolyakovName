def f(x):
	L = 3*x - 6
	M = 3*x + 99
	cnt = 10000
	while L != M and cnt:
		if L > M:
			L -= M
		else:
			M -= L
		cnt -= 1
	return M if cnt else -1


for x in range(101, 1<<20):
	if f(x) == 21:
		break

print(x)