import difflib


def str_similarity(str1, str2):
    result = difflib.SequenceMatcher(a=str1, b=str2)
    return result.ratio()


str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")
print("String similarity between 2 strings is: ", str_similarity(str1, str2))
