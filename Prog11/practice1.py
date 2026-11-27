names = ['Anna', 'Liene', 'Inga', 'Angela', 'Ilze']
ages = [19, 17, 56, 40, 7]
indexes = [0, 1, 2, 3, 4]

for index in indexes:
    status = "pilngadigs" if ages[index]>=18 else "nepilngadigs"
    print(f'{names[index]} ({status})')