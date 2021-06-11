def f(x):
	a = 3*x + 71
	b = 3*x - 87
	cnt = 1e6
	while a != b and cnt:
		if a > b:
			a -= b
		else:
			b -= a
		cnt -= 1
	return a if cnt else -1

for x in range(1, 1<<20):
	if f(x) == 158:
		break

print(x)
