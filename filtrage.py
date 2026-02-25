age = int(input("Entrez votre âge : "))
membre = input("Êtes-vous membre ? (oui/non) : ") == "oui"

if age < 18:
    print("Accès refusé")
elif age >= 18 and age < 21 and not membre:
    print("Accès autorisé, bracelet ROUGE")
elif age >= 21 or (membre and age >= 18):
    print("Accès total, bracelet VERT")