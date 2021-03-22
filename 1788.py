def algorithm(n):
	if n % 2 == 0:
		n = n*4 + 1
	else:
		n = n*4 + 2

	return n

for x in range(1, 1<<20):
	res = algorithm(x)
	if res > 138:
		break

print(x)