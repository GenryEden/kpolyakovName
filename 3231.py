def transform(s):
	while '111' in s:
		s = s.replace('111', '2', 1)
		s = s.replace('2222', '1', 1)
	return s


maximal = 0
ans = 0
for i in range(138, 1<<10):
	res = transform('1'*i).count('1')
	if res > maximal:
		maximal = res
		ans = i

print(ans)
