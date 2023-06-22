import string
# print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
# print(string.ascii_lowercase.index('a')) # 0

# prenom = 'Astrid'
# for l in prenom.lower():
#     print(f"{l} -> {string.ascii_lowercase.index(l)+1}")

# A -> 1
# s -> 19
# t -> 20
# r -> 18
# i -> 9
# d -> 4

prenom = 'Astrid'
# position_lettre = []
# for l in prenom.lower():
#     position_lettre.append(string.ascii_lowercase.index(l))
position_lettre = [string.ascii_lowercase.index(l) for l in prenom.lower()]

for(x,y) in zip(prenom, position_lettre):
    print(f"{x} -> {y+1}")
