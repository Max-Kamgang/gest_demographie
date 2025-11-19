# Crée/écrase le CSV avec des données réelles (année, population)
rows = [
    (2005, 236_000),
    (2010, 289_000),
    (2015, 353_000),
    (2020, 424_000),
    (2023, 465_000),
    (2024, 480_000),
    (2025, 496_000),
]
with open("historique_bafoussam.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["year","pop"]); w.writerows(rows)

print("historique_bafoussam.csv écrit avec données réelles (PopulationStat).")