
print("Task 1")

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

key_0 = "де"
key_1 = "при"
key_2 = "вамб"
key_3 = "глава"
key_jestkiy = "жесткийключдлятрупацанов"

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
    print(f"\n{key}:")
    CT.append(vigener_chel(text, key, alphabet))
    print(CT[-1])


print("Task 2")

def super_index(text, alphabet):
    an = 0
    n = len(text)
    for i in alphabet:
        an += (text.count(i)) * (text.count(i) - 1)

    return an/(n * (n - 1))


n = 0
for i in CT:
    print(f"{n}:")
    n += 1
    print(super_index(i, alphabet))

print("PT:\1+\+4"
      "")
print(super_index(text, alphabet))