from itertools import permutations as perm

def convert(s):
	s = ''.join(s)
	while '11' in s:
		if '112' in s:
			s = s.replace('112', '5', 1)
		else:
			s = s.replace('11', '7', 1)
	return s

ans = 0
for s in perm(25*'1' + 8*'2', 25+8):
	ans = max(sum([int(x) for x in str(ans)]), ans)
	print(ans)
	input()