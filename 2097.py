s = '>' + '1'*17 + '2'*30 + '3'*28

while '>1' in s or '>2' in s or '>3' in s:
	if '>1' in s:
		s = s.replace('>1', '22>', 1)
	if '>2' in s:
		s = s.replace('>2', '2>1', 1)
	if '>3' in s:
		s = s.replace('>3', '1>', 1)

cnt = 0
for i in s:
	try:
		cnt += int(i)
	except ValueError:
		pass

print(cnt)