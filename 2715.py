s = input()

prev = int(s[0])
cnt = 0
maxLen = 0

for i in s:
	i = int(i)
	if prev % 2 == i % 2:
		cnt += 1
	else:
		maxLen = max(maxLen, cnt)
		cnt = 0
	prev = i

print(maxLen+1)