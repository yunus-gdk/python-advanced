import re

# a = re.match(r'[a-z]+\d{2}', 'item01')
# print(a.group())

# a = re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')
# print(a.group())

# a = re.match(r'\s+', 'pierre dupont')
# print(a.group())

# a = re.match(r'\w+', 'pierre dupont')
# print(a.group())

# a = re.match(r'\w+([-+=]?)', 'pierre-dupont')
# print(a.group())

# a = re.match(r'\w+([-+=]?)', 'pierre/dupont')
# print(a.group())

a = re.match(r'\w+([-/=]+\w+)', 'pierre/dupont')
print(a.group())