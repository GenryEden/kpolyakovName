s = input()
prev = ''
beforePrev = ''
cnt = {}
for i in s:
	if i == beforePrev:
		if prev in cnt:
			cnt[prev] += 1
		else:
			cnt[prev] = 1
	beforePrev, prev = prev, i

ansLet = 'Z'
ansCnt = -1
for i in cnt:
	if cnt[i] > ansCnt or (cnt[i] == ansCnt and ansLet > i):
		ansLet = i
		ansCnt = cnt[i]
print(ansLet, ansCnt)