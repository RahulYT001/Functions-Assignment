def exp_gen(num):
    for i in range(1,num+1):
        yield i**2


a = int(input("Enter the number:\n"))
gen = exp_gen(a)
for i in gen:
    print(i)