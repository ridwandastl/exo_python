votes = {}
electeurs = set()

while True:
    id_electeur = input("Entrez votre ID (ou 'fin') : ")
    
    if id_electeur == "fin":
        break

    if id_electeur in electeurs:
        print("Déjà voté !")
        continue

    candidat = input("Votez pour (A/B/C) : ")
    electeurs.add(id_electeur)

    if candidat not in votes:
        votes[candidat] = 0
    votes[candidat] += 1
    print("Vote accepté")