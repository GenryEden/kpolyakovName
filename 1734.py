def r(n, dbg=0):
	b = bin(n)[2:]
	if dbg:
		print(b)
	b += str(sum([int(i) for i in b]) % 2)
	if dbg:
		print(b)
	b += str(sum([int(i) for i in b]) % 2)
	if dbg:
		print(b)
	return int(b, 2)

minimal = 999999
for i in range(1, 1<<10):
	res = r(i)
	if res > 90:
		minimal = min(minimal, res)	

print(minimal)