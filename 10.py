def check(str):
    for i in str:
        if i not in "aeiouAEIOU":
            return i
new = ""
str = input("Enter the string:\n")
new_str = list(filter(check, str))
for i in new_str:
    new+=i

print(new)