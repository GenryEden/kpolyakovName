def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]


for x in range(3, 10000):
	if int('121', x) + 1 == int('101', 7):
		break

print(toCountSystem(x, 3))

