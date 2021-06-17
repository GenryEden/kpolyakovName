mods = [0] + [float('inf')]*9
n = int(input())
s = 0
for i in range(n):
	a, b = map(int, input().split())
	newMods = [float('inf')]*10
	for x in a, b:
		for mod in mods:
			res = mod + x
			if res == float('inf'):
				continue
			newMods[res%10] = min(newMods[res%10], res) 
	mods = newMods
print(mods[4])