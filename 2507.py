ans = [0, '']
cnt = 1
prev = ''
s = input()
for i in s:
	if i == prev:
		cnt += 1
	else:
		if cnt > ans[0]:
			ans = [cnt, prev]
		cnt = 1
	prev = i

print(*ans[::-1])