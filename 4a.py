def insertion_sort(num_list):
    n = len(num_list)
    for i in range(1, n):
        j = i
        picked = num_list[i]
        while j > 0 and picked < num_list[j - 1]:
            num_list[j] = num_list[j - 1]
            j -= 1
            num_list[j] = picked
    return num_list


n = int(input("Enter the number of elements: "))
input_list = []
print("Enter the elements: ")
for i in range(n):
    value = int(input("Read value: "))
    input_list.append(value)

insertion_sort(input_list)
print(input_list)


def mergesort(nlist):
    if len(nlist) > 1:
        mid = len(nlist)//2
        left = nlist[:mid]
        right = nlist[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nlist[k] = left[i]
                i += 1
            else:
                nlist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nlist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nlist[k] = right[j]
            j += 1
            k += 1
    return nlist


n = int(input("Enter the number of elements: "))
nlist = []
print("Enter the elements: ")
for i in range(n):
    num = int(input())
    nlist.append(num)

mergesort(nlist)
print(nlist)


