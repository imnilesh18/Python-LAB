def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


start_range = int(input("Enter the Starting Value: "))
end_range = int(input("Enter the Ending Value: "))

prime_numbers_in_range = [number for number in range(start_range, end_range + 1) if is_prime(number)]

print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers_in_range}")

# Output:
# Enter the Starting Value: 1
# Enter the Ending Value: 50
# Prime numbers between 1 and 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
