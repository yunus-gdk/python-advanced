dic = {
    "User1:": "John",
    "User2": "Albert",
    "User3": "René"
}

for i, (cle, valeur) in enumerate(dic.items(), 1):
    print(i, cle, valeur)