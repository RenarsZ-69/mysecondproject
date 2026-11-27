a=6
b=7
c=a+b
print(c)

word="Computer"
print(word)

word1="Computer"
for l in word1:
    print(l)

for i in range(25):
    print(word)

word2="Technology"
for i in range(26):
    print(f'{i}.{word2}')

word3 = "Hello"

for x in range(1, 26):
    print(f"{x:03d}. {word3}")

with open('data.txt', 'w') as file:
    file.write('Hello!')

with open("test.txt", "w", encoding="utf-8") as file:
    for number in range(1,26):
        file.write(f"{number:02d}.{word3}\n")
        print(f"{word3}")
    file.write(f"Paldies, uz redzēšanos!")
