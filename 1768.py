def f(n):
	ans = bin(n)[2:]
	ans = ans[::-1]
	return int(ans, 2)

for x in range(501, 1<<20):
	res = f(x)
	if res == 19:
		break

print(x)