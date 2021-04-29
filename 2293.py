a = [x for x in range(3201, 12876+1) if x % 4 == 0]
a = [x for x in a if x % 7 != 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 13 != 0]
a = [x for x in a if x % 19 != 0]

print(len(a), max(a))