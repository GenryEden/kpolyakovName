def f(x):
	a = x - 61
	b = 3*x - 138
	cnt = x**2
	while a != b and cnt:
		if a > b:
			a -= b
		else:
			b -= a
		cnt -= 1
	return a if cnt else -1

for x in range(1, 1<<20):
	if f(x) == 45:
		break

print(x)