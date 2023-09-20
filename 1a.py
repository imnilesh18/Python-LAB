marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

minimum = min(marks1, marks2, marks3)
avg = ((marks1 + marks2 + marks3) - minimum)/2
print(f"The Average of Best of two: {avg}")
