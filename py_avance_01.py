import os
from time import time
from random import randint

cur_dir = os.path.dirname(__file__)
fichier_immuable = os.path.join(cur_dir, 'nombres_aleatoires_avec_immuable.txt')
fichier_muable = os.path.join(cur_dir, 'nombres_aleatoires_avec_muable.txt')
max_range = 200000

a = time()
nombre_aleatoire = ''
for i in range(max_range):
	nombre_aleatoire += str(randint(0, 9999))
	nombre_aleatoire += '\n'

with open(fichier_immuable, 'w') as f:
	f.write(nombre_aleatoire)

b = time()
print('Temps d\'execution: {}'.format(b - a))


c = time()
liste_aleatoire = []
for i in range(max_range):
	liste_aleatoire.append(randint(0, 9999))

with open(fichier_muable, 'w') as f:
	for item in liste_aleatoire:
		f.write("%s\n" % item)

d = time()
print('Temps d\'execution: {}'.format(d - c))


# correction
# c = time()
# liste_aleatoire = []
# for i in range(max_range):
# 	liste_aleatoire.append(str(randint(0, 9999)))

# with open(fichier_muable, 'w') as f:
# 	f.write('\n'.join(liste_aleatoire))

# d = time()
# print('Temps d\'execution: {}'.format(d - c))