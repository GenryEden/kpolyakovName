s = input()
cnt = 0
ans = 0
for i in s:
	if i == 'C':
		cnt += 1
	else:
		ans = max(ans, cnt)
		cnt = 0
		
ans = max(ans, cnt)
print(ans)