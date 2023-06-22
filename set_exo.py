import os
from pprint import pprint

cur_dir = os.path.dirname(__file__)

dossier_rendu_01 = os.path.join(cur_dir, 'exo_set', 'rendus_01')
dossier_rendu_02 = os.path.join(cur_dir, 'exo_set', 'rendus_02')

fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_02 = os.listdir(dossier_rendu_02)

set_fichiers = set(fichiers_01) | set(fichiers_02)
set_complet = ["000"+str(i)+".jpg" if i < 10 else "00"+str(i)+".jpg" for i in range(1,100)]
set_complet.append("0100.jpg")

pprint(set(set_complet) - set_fichiers)