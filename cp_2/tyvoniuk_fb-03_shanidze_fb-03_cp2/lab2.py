print("Task 1")

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

key_0 = "эь"
key_1 = "нрм"
key_2 = "дзкц"
key_3 = "яюьен"
key_jestkiy = "жесткийключдлятру"

with open('finaltext.txt', 'r', encoding='utf-8') as file:
    text = file.read()


def vigener_chel(plain_text, key, alphabet):
    m = len(alphabet)
    cr = ""
    for i in range(len(plain_text) - 1):
        cr += f"{alphabet[(alphabet.find(plain_text[i]) + alphabet.find(key[i % len(key)])) % m]}"
    return cr


CT = []
for key in (key_0, key_1, key_2, key_3, key_jestkiy):
    print(f"Ключ довжини {len(key)}, {key}:")
    CT.append(vigener_chel(text, key, alphabet))
    print(CT[-1])


print("Task 2")


def super_index(text: str, alphabet):
    an = 0
    n = len(text)
    for i in alphabet:
        an += (text.count(i)) * (text.count(i) - 1)

    return an/(n * (n - 1))

n = 2
for i in CT:
    if n == 6:
        n = 17
    print(f"Ключ довжини {n}:")
    n += 1
    print(super_index(i, alphabet))

print("Відкритий текст:")
print(super_index(text, alphabet))

print("Task 3")

with open('finaltextXD.txt', 'r', encoding='utf-8') as file:
    text = file.read()


def rozbivka_na_gramy(text, n):
    temp = []
    for i in range(n):
        j = i
        l = ""
        while j < len(text):
            l += text[j]
            j += n
        temp.append(l)

    return temp

mb_kluchi = []
for i in range(2, 31):
    mb_kluchi.append(rozbivka_na_gramy(text, i))

for i in mb_kluchi:
    print(i)
    print(super_index(i, alphabet))