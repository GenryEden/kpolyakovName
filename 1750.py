def auto(x):
	return 256 - x

for i in range(1, 256):
	if auto(i) == 211:
		print(i)