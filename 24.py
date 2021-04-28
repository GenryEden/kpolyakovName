def f(x):
	L = x
	M = 65
	if L % 2 == 0:
		M = 52
	while L != M:
		if L > M:
			L -= M
		else:
			M -= L
	return M

for x in range(101, 1<<20):
	if f(x) == 26:
		break

print(x)