def check(x):
	first = int(str(x)[0])
	for i in [int(n) for n in str(x)]:
		if i > first:
			return False
	return not(str(x).count('5') % 2) and str(x).count('5') >= 2

a = []
ans = 0
for x in range(1007, 746002):
	if check(x):
		if str(x)[0:2] == '50':
			ans = max(ans, x)
		a.append(x)