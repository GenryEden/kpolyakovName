def f(n):
	b = bin(n)[2:]
	b += str(sum([int(x) for x in b]) % 2)
	b += str(sum([int(x) for x in b]) % 2)
	return int(b, 2)

ans = 999
for x in range(1, 1<<10):
	if ans > f(x) > 118:
		ans = f(x)

print(ans)