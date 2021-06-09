def check(x):
	cnt = 0
	minimal = 0
	maximal = 0
	for i in range(10, 100):
		if x % i == 0:
			cnt += 1
			if cnt == 1:
				minimal = i
			maximal = i
	return cnt == 35, minimal, maximal

for x in range(333555, 777999):
	res = check(x)
	if res[0]:
		print(x, res[1], res[2])

