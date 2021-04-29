a = [x for x in range(1305, 7850+1) if x % 4 == 0 or x % 7 == 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]
a = [x for x in a if x % 21 != 0]

print(len(a), min(a))