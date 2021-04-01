s = input()
ans = {}
for x in range(len(s)-2):
	res = s[x:x+3]
	if res[0] == 'X' and res[2] == 'Z':
		if res[1] in ans:
			ans[res[1]] += 1
		else:
			ans[res[1]] = 1

keys = sorted(list(ans)) 
maxAns = 0
letAns = ''
for key in keys:
	if ans[key] > maxAns:
		letAns = key
		maxAns = ans[key]

print(letAns, maxAns, sep='')