s = input()
prevCode = -1
cnt = 0
ans = 0
cntS = 1
ansS = 1
lastS = 1

for l in s:
	code = ord(l)
	if code > prevCode:
		cnt += 1
	else:
		if cnt > ans:
			ans = cnt
			ansS = lastS
		lastS = cntS
		cnt = 0
	cntS += 1
	prevCode = code

if cnt > ans:
	ans = cnt
	ansS = lastS
	lastS = cntS

print(ansS)