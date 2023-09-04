filename = input("Enter Filename: ")
f1 = open(filename)
N = int(input("Enter the number of lines to be displayed: "))
word = input("Enter word to count its frequency of occurrence in the file: ")
line_number = 0
for line in f1:
    if line_number == N:
        break
    print(line)
    line_number = line_number + 1

f1 = open(filename)
count = 0

for line in f1:
    if word in line.split():
        print(line.split())
        count = count + 1

print("Frequency of %s is %d " % (word, count))
