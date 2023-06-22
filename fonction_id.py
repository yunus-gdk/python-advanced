liste_originale = [1,2, 3, 4]
liste_dupliquee = liste_originale

liste_originale.append(5)

print(id(liste_originale))
print(id(liste_dupliquee))

liste_dupliquee_unique = liste_originale[:]
liste_originale.append(6)

print(id(liste_originale))
print(id(liste_dupliquee))
print(id(liste_dupliquee_unique))