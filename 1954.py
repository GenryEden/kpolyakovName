from itertools import permutations
# print(list(permutations('123')))
cnt = 0
a = 0
hashes = []
for x in permutations('АВРОРА'):
	s = ''.join(x)
	a += 1
	if 'РР' not in s and 'АА' not in s:
		# print(s)
		cnt += (hash(s) not in hashes)
		hashes.append(hash(s))
print(cnt)