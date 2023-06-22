liste1 = [1, 2, 3, 4, 5]
liste_double1 = []

# for i in liste:
#     liste_double.append(i * 2)

liste_double1 = [i*2 for i in liste1]
print(liste_double1)

liste2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double2 = []

# for i in liste:
#     if i > 0:
#         liste_double.append(i * 2)
# print(liste_double)

liste_double2 = [i * 2 for i in liste2 if i > 0]
print(liste_double2)

liste3 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double3 = []

# for i in liste:
#     if i > 0:
#         liste_double.append(i * 2)
#     else:
#         liste_double.append(i * 3)

liste_double3 = [i * 2 if i > 0 else i * 3 for i in liste3]
print(liste_double3)

liste_finale = []
# for a in range(10):
#     for b in range(2):
#         liste_finale.append((a, b))
liste_finale = [(a, b) for a in range(10) for b in range(2)]
print(liste_finale)