def f(n):
	b = bin(n)[2:]
	b += str(sum([int(x) for x in str(b)]) % 2)
	b += str(sum([int(x) for x in str(b)]) % 2)
	return int(b, 2)


for x in range(1, 1<<20):
	if f(x) > 125:
		break

print(x)
