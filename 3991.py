def check(x):
	return (x % int('1010', 2))*(x % int('77', 8)) == 0 and (x % int('ff', 16) == 0)

cnt = 0
minimal = 0

for x in range(1000, 10001+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal)