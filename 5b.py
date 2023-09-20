import re

ph_regex = re.compile(r'\+\d{12}')
mail_regex = re.compile(r'\S+\@\S+')

with open('testfile.txt', 'r') as f:
    for line in f:
        pmatches = ph_regex.findall(line)
        for match in pmatches:
            print(match)
        ematches = mail_regex.findall(line)
        for match in ematches:
            print(match)
