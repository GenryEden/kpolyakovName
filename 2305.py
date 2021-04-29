a = [x for x in range(1221, 9763+1) if x % 7 == 0]
a = [x for x in a if x % 2 != 0]
a = [x for x in a if x % 5 != 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 49 != 0]

print(len(a), max(a))