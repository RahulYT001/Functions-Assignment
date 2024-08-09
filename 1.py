def sum_even(l):
    a = list(filter(lambda x: x%2==0, l))
    sum = reduce(lambda x,y : x+y, a)
    print(sum)


from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even(l)