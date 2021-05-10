s = input()
prev = ''
cnt = 1
ans = 0

for i in s:
	if i != prev:
		cnt += 1
	else:
		ans = max(ans, cnt)
		cnt = 1
	prev = i

ans = max(ans, cnt)
print(ans)