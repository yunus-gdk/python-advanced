import re

texte = "item 01 | item02 - item03 - item04 | item05"

a = re.split(r' \| | - ', texte)
print(a)