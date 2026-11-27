word = 'Item'
with open('items.txt', 'w', encoding="utf-8") as file:
    for number in range(1, 101):
        file.write(f'{word} {number}\n')