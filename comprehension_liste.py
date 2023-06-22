liste = [-3, -2, -1, 0, 1, 2, 3]

print([i+1 for i in liste if i > 0])

print([i+1 if i > 0 else i-2 for i in liste])

liste2= [-3, -2, -1, 0, 1, 2, 3]
liste_double=[i*2 for i in liste2]
print(liste_double)