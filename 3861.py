def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

for x in range(1, 1<<20):
	if sumOfNumerals(toCountSystem(27**7 - 3**11 + 36 - x, 3)) == 22:
		break

print(x)