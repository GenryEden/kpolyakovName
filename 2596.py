def check(x):
	for i in str(x):
		if int(i) % 2 == 0:
			return False
	return True

def sumOfNumerals(x):
	return sum([int(i) for i in str(x)])

ans = 0

for x in range(1686, 13276+1):
	if check(x):
		ans += sumOfNumerals(x)

print(ans)