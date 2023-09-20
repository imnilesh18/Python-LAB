import re


def isphonenumber(numstr):
    if len(numstr) != 12:
        return False
    for i in range(0, 3):
        if not numstr[i].isdigit():
            return False
    if numstr[3] != "-":
        return False
    for i in range(4, 7):
        if not numstr[i].isdigit():
            return False
    if numstr[7] != '-':
        return False
    for i in range(8, 12):
        if not numstr[i].isdigit():
            return False
    return True


def isphnum(numstr):
    ph_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_pattern.match(numstr):
        return True
    else:
        return False


nstr = input("Enter the Phone Number: ")

print("Without using Regular expression: ")
if isphonenumber(nstr):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

print("With Regular Expression: ")
if isphnum(nstr):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
