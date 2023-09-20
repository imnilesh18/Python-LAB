str1 = input("Enter the String: ")
words = str1.split()
uppercase_count = 0
lowercase_count = 0
digit_count = 0

for char in str1:
    if char.isalpha():
        if char.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Number of Words: {len(words)}")
print(f"Number of Digits: {digit_count}")
print(f"Number of UpperCase letters: {uppercase_count}")
print(f"Number of LowerCase letters: {lowercase_count}")
