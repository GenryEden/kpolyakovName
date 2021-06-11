def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

for x in range(1, 1<<20):
	res = toCountSystem(81**20 - 9**x + 50, 9)
	if sumOfNumerals(res) == 138:
		break

print(x)