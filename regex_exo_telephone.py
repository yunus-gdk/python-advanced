import re

numeros_de_telephone = ['06-71-45-34-23',
						'02-12-33-75-12',
						'00-23-14-52-44',
						'03-52-31-56-34',
                        '514-235-0293']

# Le numéro 06-71-45-34-23 est valide
# Le numéro 02-12-33-75-12 est valide
# Le numéro 00-23-14-52-44 est invalide
# Le numéro 514-235-0293 est invalide
# Le numéro 03-52-31-56-34 est valide

# Un numéro valide en France doit être composée d'une suite de 5 nombres avec 2 chiffres.
# La première série de nombres doit être comprise entre 01 et 07.

# Cela donne donc 0A-XX-XX-XX-XX où A est un nombre compris entre 1 et 7 et X un nombre compris entre 0 et 9.

# a = re.match(r'(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})', "06-71-45-34-23")


for i in numeros_de_telephone:
    a = re.match(r'(0[1-7])(-(\d{2})){4}', i)
    print(f"{a.group()} valide.") if a is not None else print(f"{i} invalide !!!")
