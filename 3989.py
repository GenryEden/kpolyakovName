def check(x):
	if (x % int('20', 8))*(x % int('30', 16)) != 0:
		return False
	if x % int('10', 2) == 0:
		return True
	return bool((x % int('11', 2))*(x % int('22', 8))*(x % int('3f', 16)))

cnt = 0
minimal = 0

for x in range(1110, 1111101):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x
print(cnt, minimal)