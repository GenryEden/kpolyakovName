def f(x):
	a = 2*x - 91
	b = 3*x - 159
	cnt = x**2
	while a != b and cnt:
		cnt -= 1
		if a > b:
			a -= b
		else:
			b -= a
	return a if cnt else -1

for x in range(1, 1<<20):
	if f(x) == 15:
		break

print(x)