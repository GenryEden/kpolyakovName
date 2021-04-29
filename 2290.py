a = [x for x in range(1016, 7937+1) if x % 3 == 0]
a = [x for x in a if x % 7 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]
a = [x for x in a if x % 27 != 0]
print(len(a), max(a))