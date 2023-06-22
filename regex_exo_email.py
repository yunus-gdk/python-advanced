import re

# 0{1}[1-7]{1}(-[0-9]{2}){4}
# 06-71-45-34-23
 
adresses_mail = ['christian_martin@gmail.com',
                 'JaiOublieLarobasegmail.com',
                 'MarieHutchinson03523@yahoo.co.uk',
                 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
                 'ceciNestPasUneDresseMail']
 
# L'adresse christian_martin@gmail.com est valide
# L'adresse JaiOublieLarobasegmail.com est invalide
# L'adresse MarieHutchinson03523@yahoo.co.uk est valide
# L'adresse UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com est valide
# L'adresse ceciNestPasUneDresseMail est invalide

for i in adresses_mail:
    a = re.match(r'(.+)@{1}(\w+)((\.)\w+)', i)
    print(f"{a.group()} valide.") if a else print(f"{i} invalide !!!")