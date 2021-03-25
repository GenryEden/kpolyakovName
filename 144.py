def avtomat(x):
	s = [int(i) for i in str(x)]
	assert len(s) == 5
	ans = []
	ans.append(s[0] + s[2] + s[4])
	ans.append(s[1] + s[3])
	return int(''.join([str(i) for i in sorted(ans)]))

for x in range(10000, 99999):
	if avtomat(x) == 621:
		break
print(x)