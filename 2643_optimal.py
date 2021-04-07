memory = {}
n = int(input())

for _ in range(n):
	inp = int(input())
	if inp in memory:
		memory[inp] += 1
	else:
		memory[inp] = 1
ans = 0
for x in memory:
	if 100 - x in memory:
		ans += min(memory[x], memory[100-x])

ans //= 2
print(ans)