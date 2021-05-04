def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

for x in range(2, 17):
	if toCountSystem(94, x)[-3:-1] == '23':
		break

print(x)