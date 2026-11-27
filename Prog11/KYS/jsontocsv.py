import csv

json_data = {
    "darbinieki": [
        {"darbiniekaID": 8546957, "vards": "Jānis", "uzvards": "Andersons", "departaments": "Pārdošanas Departaments"},
        {"darbiniekaID": 98468574, "vards": "Anna", "uzvards": "Bērziņa", "departaments": "Marketinga departaments", "pilseta": "Jelgava"}
    ]
}

rows = json_data["darbinieki"]

fieldnames = set()
for row in rows:
    fieldnames.update(row.keys())
fieldnames = sorted(list(fieldnames))

with open("darbs.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("CSV file created successfully!")
