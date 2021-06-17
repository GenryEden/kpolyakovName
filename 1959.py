from itertools import permutations

ans = set()

for word in permutations('АССАСИН'):
	word = ''.join(word)
	ans.add(word)

print(len(ans))