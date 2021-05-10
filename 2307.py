a = [int(x) for x in range(3672, 9117+1) if x % 3 == 2]
a = [int(x) for x in a if x % 5 == 4]
print(len(a), sum(a))