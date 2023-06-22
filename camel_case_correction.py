phrase = 'Phrase en camel case'
mots = phrase.lower().split(' ')
phrase_convertie = mots[0]
for i, mot in enumerate(mots):
    if i > 0:
        phrase_convertie += mot.capitalize()
print(phrase_convertie)

phrase = 'Phrase en camel case'
mots = phrase.lower().split(' ')
phrase_convertie = mots.pop(0)
for mot in mots:
    phrase_convertie += mot.capitalize()
print(phrase_convertie)