def fibonacci_gen(n):
    a = 0
    b = 1
    print(a,b,end=",")
    count = 0
    while count < n:
        c = a+b
        a = b
        b = c
        count+=1
        yield c

n = int(input("Enter the number:\n"))
fib = fibonacci_gen(n)
for i in fib:
    print(i,end=",")