def countDels(x):
	cnt = 0
	last = 0
	for i in range(1, x):
		if x % i == 0:
			last = i
			cnt += 1
	return cnt+1, last

for x in range(164700, 164752+1):
	cnt, last = countDels(x)
	if cnt == 6:
		print(last, x)
