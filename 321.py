def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

for x in range(2, 17):
	s = toCountSystem(30, x)
	if len(s) == 4 and s[-1] == '0':
		break
print(x)