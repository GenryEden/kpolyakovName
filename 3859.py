for x in range(1, 1<<20):
	res = oct(64**12 - 8**14 + x)[2:]
	if res.count('7') == 12 and res.count('1') == 1:
		break

print(x)