distances = [150, 230, 310, 80]

total = sum(distances)

carburant = (total * 8 / 100) * 1.90

pauses = 0
cumul = 0
prochain_arret = 400

for d in distances:
    cumul += d
    if cumul >= prochain_arret:
        pauses += 1
        prochain_arret += 400

print(f"Distance totale : {total} km")
print(f"Budget carburant : {carburant:.2f} €")
print(f"Pauses : {pauses} pause(s)")