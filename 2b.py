n = input("Enter the binary number: ")
if not all(bit in ('0', '1') for bit in n):
    print("Invalid input: Not a Binary Number.")
else:
    print("Decimal value is: ", int(n, 2))

oct_num = input("Enter Octal Number: ")
h = hex(int(oct_num, 8))
print("Hexadecimal value is: ", h)
