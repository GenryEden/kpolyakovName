def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

print(sum([int(i) for i in toCountSystem(9**5 + 3**25 - 20, 3)]))