def addition(*args):
	return sum(args)
print(addition(5, 2, 8, 4))


couleur_dic = {"rouge": 255, "vert": 0, "bleu": 0}
def afficher(**kwargs):
	return kwargs.keys()
print(afficher(**couleur_dic))