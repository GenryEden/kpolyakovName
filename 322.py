for x in range(6, 1<<20):
	ix = int('225', x)
	y = 6
	iy = int('405', y)
	while iy < ix:
		y += 1
		iy = int('405', y)
	if iy == ix:
		break

print(x)