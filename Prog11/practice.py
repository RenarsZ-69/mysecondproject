import json
with open ('dati.txt','w', encoding='utf-8') as file:
    while True:
        vards=input("Ieraksti vārdu:")
        file.write(f'{vards} \n')
        print(f'{vards}')
        if vards == "00":
            break
    file.write(f"Paldies, uz redzēšanos! \n")
