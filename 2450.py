def f(x):
	Q = 6
	L = 0
	while x >= Q:
		L += 1
		x -= Q
	M = x
	if M < L:
		M = L
		L = x
	return L, M
last = 0
for x in range(1, (1<<10)):
	res = f(x)
	if res[0] == 3 and res[1] == 5:
		last = x

print(last)