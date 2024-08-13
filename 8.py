def sort(l):
    a = sorted(l, key = lambda x: x[1])
    return a

my_tuples = [(1, 3), (4, 1), (2, 2), (5, 0)]
print(sort(my_tuples))