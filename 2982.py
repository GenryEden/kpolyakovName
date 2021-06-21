n = int(input())
mem = {}
for i in range(n):
	x = str(int(input()))
	if x in mem:
		mem[x] += 1
	else:
		mem[x] = 1
cnt = 0
mid = 0
for i in mem:
	if i != i[::-1]:
		if i[::-1] not in mem:
			continue
		toAdd = min(mem[i], mem[i[::-1]])
		cnt += toAdd*sum([int(x) for x in i])
	else:
		if mem[i] % 2 == 0:
			toAdd = mem[i]
			cnt += toAdd*sum([int(x) for x in i])
		else:
			toAdd = mem[i] - 1
			cnt += toAdd*sum([int(x) for x in i])
			mid = max(mid, int(i))

print(cnt + sum([int(l) for l in str(mid)]))