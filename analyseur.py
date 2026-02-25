logs = ["user:admin:fail", "user:lucas:success", 
        "user:admin:fail", "user:admin:fail", "user:lucas:fail"]

stats = {}
blacklist = []

for log in logs:
    parties = log.split(":")
    utilisateur = parties[1]
    statut = parties[2]

    if statut == "fail":
        if utilisateur not in stats:
            stats[utilisateur] = 0
        stats[utilisateur] += 1

        if stats[utilisateur] >= 3 and utilisateur not in blacklist:
            blacklist.append(utilisateur)

print("Stats :", stats)
print("Blacklist :", blacklist)