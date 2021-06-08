def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

ans = 0
for x in range(2031, 14312+1):
	if not '2' in toCountSystem(x, 11):
		ans = x
print(ans)