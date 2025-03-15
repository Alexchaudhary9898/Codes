string = input("pls enter your own string: ")

string2 = ('')
for i in string:
    string2 = i + string2

print("\nThe original string = ", string)
print("the reversed string = ", string2)