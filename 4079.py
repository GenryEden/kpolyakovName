def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x%y)[2:]
		x //= y
	return ans[::-1]

print(sum([int(i) for i in toCountSystem(5*216**1256 - 5*36**1146 + 4*6**1053 - 1087, 6)]))