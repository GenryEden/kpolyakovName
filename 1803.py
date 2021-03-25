def f(s):
	n = 5
	while n > 0:
		s += n
		n -= 1
	return s
last = 0
for x in range(1, 1<<20):
	res = f(x)
	if res <= 550:
		last = x

print(last)