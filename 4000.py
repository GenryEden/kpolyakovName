def f(x):
	a = 5*x + 345
	b = 5*x - 807
	cnt = 100000
	while a != b and cnt:
		cnt -= 1
		if a > b:
			a -= b
		else:
			b -= a
	return a


for x in range(1, 1<<20):
	if f(x) == 96:
		break

print(x)