# main.py

a = 78
b = 90
c = 91

# if statement
if a > 70:
    print("above 70")
    if a > 80:
        print("also above 80")
    else:
        print("not above 80")

# Ternary operator
print("a is greater than b") if a > b else print("nothing")

# Nested if-else statement
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
