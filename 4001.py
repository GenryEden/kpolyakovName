def f(x):
	a = 3*x + 67
	b = 3*x - 61
	cnt = 100000
	while a != b and cnt:
		if a > b:
			a -= b
		else:
			b -= a
		cnt -= 1
	return a

for x in range(2, 1<<20):
	if f(x) == 64:
		break

print(x)