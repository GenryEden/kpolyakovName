def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

for x in range(1, 1<<20):
	if sumOfNumerals(toCountSystem(64**11 - 4**10 + 96 - x, 4)) == 71:
		break

print(x)