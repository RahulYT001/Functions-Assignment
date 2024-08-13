def one_line_gen(file):
    with open(f"{file}", "r") as f1:
        lines = f1.readlines()
        for i in lines:
            yield i
a = input("Enter the file name with the extension. Eg:- file.txt\n")
lines = one_line_gen(a)
for i in lines:
    print(i)
    