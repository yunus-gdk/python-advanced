phrase = 'Phrase en camel case' # Convertir la phrase ci-dessus dans ce format : phraseEnCamelCase
liste = phrase.lower().split()
camel_case = ""
for i, item in enumerate(liste):
    if i > 0:
        camel_case += item.capitalize()
print(liste[0]+camel_case)
