def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

for y in range(2, 1<<20):
	res = toCountSystem(71, y)
	if res[-2:] == '13':
		break

print(y)