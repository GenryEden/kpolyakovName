def cntDels(x):
	cnt = 0
	for i in range(1, x+1):
		if x % i == 0:
			cnt += 1
	return cnt
	
ans = [0,0]
for x in range(394441, 394505+1):
	cnt = cntDels(x)
	if cnt > ans[0]:
		ans = [cnt, x]

print(*ans)
