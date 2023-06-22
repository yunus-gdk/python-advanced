multiplication = lambda a, b: a * b
resultat = multiplication(5, 10)
print(resultat)

print_mot = lambda m: print(m)
print_mot("Python")

###############################################

import os
fichiers = ['/H/Projets/fichier1.py',
		    '/H/Projets/fichier2.pptx',
		    'Y/Dossiers/fichier3.txt']

get_fichier = lambda f: os.path.split(f)[-1]
get_ext = lambda f: os.path.splitext(f)[-1]
del_point = lambda f: f.replace('.', '')
process = lambda f: del_point(get_ext(get_fichier(f)))

# fichiers_extensions = [os.path.splitext(os.path.split(f)[-1])[-1].replace('.', '') for f in fichiers]
fichiers_extensions = [process(f) for f in fichiers]
print(fichiers_extensions)

###############################################

utilisateurs = [("User1", "Etienne"),
                ("User4", "Arnaud"),
                ("User3", "Camille"),
                ("User5", "Bernard"),
                ("User2", "Didier")]
utilisateurs.sort()
# ("User1", "Etienne"),("User2", "Didier"),("User3", "Camille"),("User4", "Arnaud"),("User5", "Bernard")
utilisateurs.sort(key=lambda x: x[1])
# ("User4", "Arnaud"),("User5", "Bernard"),("User3", "Camille"),("User2", "Didier"),("User1", "Etienne")
print(utilisateurs)