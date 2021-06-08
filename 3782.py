file = open('24-s1.txt')
cnt, ans = 0, 0

for i, line in enumerate(file):
    cntLine = line.count('Q')
    if cntLine >= cnt:
        cnt, ans = cntLine, i


file.close()
file = open('24-s1.txt')
lines = [line[:-1] for line in file.readlines()]
cntSymb, ansSymb = float('inf'), ''

for s in set(lines[ans]):
    if (lines[ans].count(s) < cntSymb) or (lines[ans].count(s) == cntSymb and s < ansSymb):
        cntSymb, ansSymb = lines[ans].count(s), s
file.close()

file = open('24-s1.txt')
print(ansSymb, file.read().count(ansSymb))
file.close()
