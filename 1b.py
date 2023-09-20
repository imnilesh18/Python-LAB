num = input("Enter the number: ")
rev = num[::-1]
print(rev)

if rev == num:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")

num = int(num)
freq = {}
while num != 0:
    digit = num % 10
    if digit in freq:
        freq[digit] = freq[digit] + 1
    else:
        freq[digit] = 1
    num = num // 10
print(freq)
