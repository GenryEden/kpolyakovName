def r(n):
	b = bin(n)[2:]
	b += str(sum([int(i) for i in b]) % 2)
	b += str(sum([int(i) for i in b]) % 2)
	return int(b, 2)

ans = set()

for x in range(1, 1<<10):
	res = r(x)
	if res > 80:
		ans.add(res)
print(min(ans))