def transform(s):
	while '111' in s:
		s = s.replace('111', '2', 1)
		s = s.replace('2222', '333', 1)
		s = s.replace('33', '1', 1)
	return s

maximalCnt = 0
ans = 0

for i in range(91, 1<<11):
	res = transform('1'*i).count('1')
	if res > maximalCnt:
		ans = i
		maximalCnt = res

print(ans)