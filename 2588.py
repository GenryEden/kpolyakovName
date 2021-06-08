def isNice(x):
	s = 0
	cnt = 0
	for i in range(1, x):
		if x % i == 0:
			s += i
			cnt += 1
	return s == x, cnt

for x in range(2, 10000+1):
	res = isNice(x)
	if res[0]:
		print(x, res[1])
