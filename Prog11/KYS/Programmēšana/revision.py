import csv
import json

csv_filename = "darbinieki.csv"
headers = ["darbiniekaID", "vards", "uzvards", "departaments", "pilseta"]

data = [
    [8546957, "Jānis", "Andersons", "Pārdošanas Departaments", ""],
    [98468574, "Anna", "Bērziņa", "Marketinga departaments", "Jelgava"],
    [12345678, "Juris", "Ozoliņš", "IT departaments", "Rīga"],
    [87654321, "Liene", "Kalniņa", "Finanšu departaments", "Valmiera"]
]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"CSV fails '{csv_filename}' ir veiksmīgi izveidots.")

darbinieku_saraksts = []

with open(csv_filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["darbiniekaID"] = int(row["darbiniekaID"])
        
        if not row["pilseta"]:
            del row["pilseta"]
            
        darbinieku_saraksts.append(row)

json_data = {"darbinieki": darbinieku_saraksts}
json_filename = "darbinieki.json"
with open(json_filename, mode="w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)

print(f"JSON fails '{json_filename}' ir veiksmīgi izveidots.")
