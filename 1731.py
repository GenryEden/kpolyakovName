def r(n, dbg=0):
	b = bin(n)[2:]
	if dbg:
		print(b)
	s = sum([int(i) for i in b])
	b += str(s % 2)
	if dbg:
		print(b)
	s = sum([int(i) for i in b])
	b += str(s % 2)
	if dbg:
		print(b)
	return int(b, 2)
ans = set()
for x in range(1, 1<<10):
	res = r(x)
	if res < 80:
		ans.add(res)

print(len(ans))