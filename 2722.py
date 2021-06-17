for x in range(4, 1<<20):
	left = int('21', x) * int('13', x)
	right = int('313', x)
	if left == right:
		break

print(x)