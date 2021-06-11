def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

cnt = 0
maximal = 0

for x in range(198372, 876193+1):
	if x % sumOfNumerals(x) == 11:
		cnt += 1
		maximal = x

print(cnt, maximal)