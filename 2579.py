def cntDels(x):
	cnt = 1
	lastDel = 0
	for i in range(1, x//2+1):
		if x % i == 0:
			cnt += 1
			lastDel = i
	return cnt, lastDel

ans = [0,0]
maxCnt = 0
for x in range(286564, 287270+1):
	res = cntDels(x)
	if res[0] >= maxCnt:
		maxCnt = res[0]
		ans = [x, res[1]]

print(maxCnt, ans[1])