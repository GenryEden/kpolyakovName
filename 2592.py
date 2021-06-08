def sumOfNumerals(x):
	return sum([int(i) for i in str(x)])

def multOfNumerals(x):
	ans = 1
	for i in str(x):
		ans *= int(i)
	return ans

toAns = []
for x in range(87921, 88187+1):
	s = sumOfNumerals(x)
	m = multOfNumerals(x)
	if s % 14 == 0 and m % 18 == 0 and m != 0:
		toAns.append([s, m])

toAns.sort(key=lambda x: x[1])
for i in toAns:
	print(*i)