def sumOfNumerals(x):
	return sum([int(i) for i in str(x)])

def mulOfNumerals(x):
	ans = 1
	for i in [int(n) for n in str(x)]:
		ans *= i
	return ans
toAns = []
for i in range(87921, 88187+1):
	s = sumOfNumerals(i)
	m = mulOfNumerals(i)
	if s % 14 == 0 and m % 18 == 0 and m != 0:
		toAns.append([s, m])

toAns.sort(key= lambda x: x[1])
for i in toAns:
	print(*i)