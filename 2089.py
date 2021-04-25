s = 50*'1' + 50*'2' + 50*'3'

while ('12' in s) or ('32' in s) or ('31' in s):
	if '12' in s:
		s = s.replace('12', '21', 1)
	if '32' in s:
		s = s.replace('32', '23', 1)
	if '31' in s:
		s = s.replace('31', '13', 1)

print(s[20-1], s[80-1], s[120-1], sep='')