def f(x):
	cnt = x**2
	a = 3*x - 112
	b = 3*x + 58
	while a != b and cnt:
		if a > b:
			a -= b
		else:
			b -= a
		cnt -= 1
	return a if cnt else -1

for x in range(1, 1<<20):
	if f(x) == 34:
		break

print(x)