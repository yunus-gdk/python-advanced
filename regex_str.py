import re

a = re.match(r'.+', 'Pierre Dupont')
print(a.group())

a = re.match(r'(\w+)\s(\w+)', 'Pierre Dupont')
print(a.group(0))
print(a.group(1))
print(a.group(2))

a = re.match(r'(?P<prenom>\w+) (?P<nom>\w+)', 'Pierre Dupont')
print(a.group('prenom'))
print(a.group('nom'))

print(a.groups())
print(a.groupdict())
