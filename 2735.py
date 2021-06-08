a = [int(x) for x in range(3232, 8299+1) if x % 2 == 0 or x % 7 == 0]
a = [x for x in a if x % 15 != 0]
a = [x for x in a if x % 28 != 0]
a = [x for x in a if x % 41 != 0]
print(len(a), sum(a))