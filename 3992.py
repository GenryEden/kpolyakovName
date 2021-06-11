def check(x):
	return sum([int(s) for s in str(x)]) == 5 and '0' in str(x)

cnt = 0
maximal = 0
for x in range(3212, 64212+1):
	if check(x):
		maximal = x
		cnt += 1

print(cnt, maximal)