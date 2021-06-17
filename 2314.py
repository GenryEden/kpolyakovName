a = [x for x in range(1213, 8310+1) if x % 3 == 0]
a = [x for x in a if x % 23 != 0]

print(len(a), sum(a))