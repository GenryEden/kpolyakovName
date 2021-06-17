def longestLine(s):
	prev = ''
	cnt = 1
	ans = ['', 0]
	for i in s:
		if prev == i:
			cnt += 1
		else:
			if cnt > ans[1]:
				ans = [prev, cnt]
			cnt = 1
		prev = i
	if cnt > ans[1]:
		ans = [prev, cnt]
	return ans[::-1]

def getMostFreq(s):
	ans = ''
	maxCnt = 0
	for l in set(s):
		res = s.count(l)
		if res > maxCnt:
			maxCnt = res
			ans = l
		elif res == maxCnt and l < ans:
			maxCnt = res
			ans = l
	return ans, maxCnt

file = open('24-164.txt')
lines = file.readlines()
maxLen = 0
ansi = 0
for i, line in enumerate(lines):
	res = longestLine(line)
	if res[0] > maxLen:
		maxLen = res[0]
		ansi = i

letter = getMostFreq(lines[ansi])[0]

print(letter, sum([s.count(letter) for s in lines]))