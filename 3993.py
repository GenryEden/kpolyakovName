def check(x):
	return sum([int(s) for s in str(x)]) > 12 and '0' in str(x)

s = 0
cnt = 0
for x in range(2125, 665123+1):
	if check(x):
		s += x
		cnt += 1

print(cnt, s % 10000)