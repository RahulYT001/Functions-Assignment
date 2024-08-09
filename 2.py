def rev_string(str):
    rev_str = ""
    letters = []
    for i in str:
        letters.append(i)
    letters.reverse()
    for i in letters:
        rev_str += i
    return rev_str

a = "Hello"
print(rev_string(a))
