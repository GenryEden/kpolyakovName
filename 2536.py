s = input()

cnt = 0
ansN = 1
maxCnt = 0
lastN = 0
prevCode = float('inf')

for n, code in enumerate(s):
	code = ord(code)
	if code < prevCode:
		cnt += 1
	else:
		if cnt > maxCnt:
			maxCnt = cnt
			ansN = lastN
		lastN = n
		cnt = 0
	prevCode = code

if cnt > maxCnt:
	maxCnt = cnt
	ansN = lastN
	
print(ansN+1)