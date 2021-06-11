def check(x):
	return sum([int(s) for s in str(x)]) == 10 and '0' in str(x)

cnt = 0
minimal = 0

for x in range(4616, 52311+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal)