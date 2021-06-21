a = [x for x in range(1705, 7474+1) if x % 11 == 0]
a = [x for x in a if x % 19 != 0]

print(len(a), sum(a))