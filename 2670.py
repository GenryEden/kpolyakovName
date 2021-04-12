n = int(input())
mods = [0]+[float('-inf')]*3

for _ in range(n):
	a, b, c = map(int, input().split())
	newMods = [float('-inf')]*4
	for x in mods:
		for y in a, b, c:
			res = x + y
			try:
				newMods[res%4] = max(newMods[res%4], res)
			except TypeError:
				pass
	mods = newMods[:]

print(max(mods[1:]))
