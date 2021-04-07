line = input()
cnt = 0
for length in range(7, 11):
	for x in range(len(line)-length+1):
		y = x + length
		s = line[x:y]
		if s[0] == 'A' and s[-1] == 'F':
			cnt += 1
		
print(cnt)