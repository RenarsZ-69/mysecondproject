import csv

with open("edieni.csv", "r", encoding="utf-8-sig", newline="") as fails:
    dati = csv.DictReader(fails, delimiter=";")
    rindu_saraksts = list(dati) #saglabā rindas kamēr falis atverts
    for rinda in rindu_saraksts:
        if rinda["Pieejams"] == "Jā":
            print(rinda["Nosaukums"], "-", rinda["Cena_EUR"], "EUR")
print("===================")
for rinda in rindu_saraksts:
    if rinda["Pieejams"] == "Jā" and float(rinda["Cena_EUR"]) <= 6.0:
        print(f"- {rinda['Nosaukums']} ({rinda['Cena_EUR']} EUR)")
print("===================")
for rinda in rindu_saraksts:
    if rinda["Kategorija"]== "Pamatēdiens" and float(rinda["Svars_g"]) > 300:
        print(f"- {rinda['Nosaukums']} ({rinda['Cena_EUR']} EUR)")
print("===================")
for rinda in rindu_saraksts:
    if float(rinda["Kalorijas_kcal"]) < 400:
        print(f"- {rinda['Nosaukums']} ({rinda['Cena_EUR']} EUR)")
print("===================")
for rinda in rindu_saraksts:
    if float(rinda["Pagatavosanas_laiks_min"]) <= 15:
        print(f"- {rinda['Nosaukums']} ({rinda['Cena_EUR']} EUR)")
print("===================")
visdargakais = max(rindu_saraksts, key=lambda r: float(r["Cena_EUR"]))
visletakais = min(rindu_saraksts, key=lambda r: float(r["Cena_EUR"]))

print(f"Visdārgākais produkts: {visdargakais['Nosaukums']} ({visdargakais['Cena_EUR']} EUR)")
print(f"Vislētākais produkts: {visletakais['Nosaukums']} ({visletakais['Cena_EUR']} EUR)")
print("===================")

kopeja_cena = 0.0
pieejamo_skaits = 0

for rinda in rindu_saraksts:
    if rinda["Pieejams"] == "Jā":
        cena = float(rinda["Cena_EUR"])
        kopeja_cena += cena
        pieejamo_skaits += 1

if pieejamo_skaits > 0:
    videja_cena = kopeja_cena / pieejamo_skaits
    print(f"Pieejamo produktu vidējā cena: {videja_cena:.2f} EUR")
print("===================")
kategoriju_skaits = {}

for rinda in rindu_saraksts:
    kat = rinda["Kategorija"]
    if kat not in kategoriju_skaits:
        kategoriju_skaits[kat] = 0
    kategoriju_skaits[kat] += 1

print("Produktu skaits kategorijās:")
for kat, skaits in kategoriju_skaits.items():
    print(f"- {kat}: {skaits}")
print("===================")
tikai_deserti = []
for rinda in rindu_saraksts:
    if rinda["Kategorija"] == "Deserts":
        tikai_deserti.append(rinda)
n = len(tikai_deserti)
for i in range(n):
    for j in range(0, n - i - 1):
        kalorijas1 = float(tikai_deserti[j]["Kalorijas_kcal"])
        kalorijas2 = float(tikai_deserti[j + 1]["Kalorijas_kcal"])
        if kalorijas1 > kalorijas2:
            tikai_deserti[j], tikai_deserti[j + 1] = tikai_deserti[j + 1], tikai_deserti[j]
for rinda in tikai_deserti:
    print(f"- {rinda['Nosaukums']} ({rinda['Kalorijas_kcal']} kcal)")
print("===================")
for rinda in rindu_saraksts:
    if int(rinda["Pagatavosanas_laiks_min"]) <= 20 and float(rinda["Cena_EUR"]) < 8.0:
        print(f"- {rinda['Nosaukums']} ({rinda['Cena_EUR']} EUR)")
print("===================")
if len(rindu_saraksts) > 0:
    kolonnu_nosaukumi = rindu_saraksts[0].keys()
    
    with open("pieejamie_edieni.csv", "w", encoding="utf-8", newline="") as jauns_fails:
        rakstitajs = csv.DictWriter(jauns_fails, fieldnames=kolonnu_nosaukumi, delimiter=";")
        rakstitajs.writeheader()
        for rinda in rindu_saraksts:
            if rinda["Pieejams"] == "Jā":
                rakstitajs.writerow(rinda)


