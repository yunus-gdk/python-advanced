from random import randint

def lettre_random(nom):
    nom_liste = list(nom)
    for _ in range(len(nom)):
        rand_index = randint(0, len(nom_liste) - 1)
        # print(nom_liste[rand_index])
        yield nom_liste.pop(rand_index)

# a = lettre_random("bonjour")
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

new_str = "".join([letter for letter in lettre_random("bonjour")])
print(new_str)