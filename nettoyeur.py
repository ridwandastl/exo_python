utilisateurs = [" alice ","BOB","charlie","ALICE","Eve","DAN"]
utilisateurs_propres =[]
for nom in utilisateurs:
    nom_propre = nom.strip().lower()
    if nom_propre == "eve":
       break
    if nom_propre not in utilisateurs_propres:
      utilisateurs_propres.append(nom_propre)
print(utilisateurs_propres) # ['alice', 'bob', 'charlie']
    
    