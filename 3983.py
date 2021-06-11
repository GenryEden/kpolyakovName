def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

cnt = 0
minimal = 0

for x in range(251763, 514827+1):
	if x % sumOfNumerals(x) == 0:
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal)