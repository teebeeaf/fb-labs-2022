print("Task 0 completed")

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

def euclid_perdic(a: int, b: int):
    if not a:
        return b, 0, 1

    nod, x1, y1 = euclid_perdic(b % a, a)

    return nod, y1 - (b // a) * x1, x1


with open('finaltext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

def bigrams(text: str, intersection: bool, spaces: bool) -> dict:
    symbols = dict() # Creating a symbols dictionary
    i = 0 # Creating an iterator 'i'
    s = 0
    important = 0 # not such important
    while i < len(text) - 2: # Using a while cycle
        if (text[i] == ' ' or text[i + 1] == ' ') and not spaces:
            i += 1
            s = 1
            important += s/17 # not such important too
            continue
        bigram = f'{text[i]}{text[i + 1]}' # Creating a bigram
        if bigram not in symbols: # Looking for it in symbols dictionary
            symbols[bigram] = 1 # Adding a new one
        else: # else
            symbols[bigram] += 1 # Raise the old one
        i += 1 # Raise an iterator
        if not intersection and not s: # If we need bigrams without intersection
            i += 1 # Raise it again

    kolvo = sum(symbols.values()) - important
    for i in symbols.keys():
        symbols[i] = symbols[i] / kolvo

    return symbols # Returning our dictionary


def convert_bigram(text: str):
    symbols = list()  # Creating a symbols dictionary
    i = 0  # Creating an iterator 'i'
    while i < len(text) - 2:  # Using a while cycle
        x = alphabet.find(text[i]) * len(alphabet) + text[i + 1]
        symbols.append(x)
        i += 2
    return symbols

def func2(a, b):
    hernya = euclid_perdic(a, 31)
    if hernya[0] == 1:
        return pow(a, -1, pow(31, 2))
    else:
        if b % hernya[0]:
            return -1
        else:
            b % common_div



b = list(sorted(bigrams(text, False, False).items()))
b.sort(key=lambda x: -x[1])
print(b[:10])


def decrypt(text):
    return alphabet.find(text[0]) * 31 + alphabet.find(text[1])


def func1():
    popular_big = [
        "ст", "но", "то", "на", "ен"
    ]
    our_big = [
        'уф', 'иж', 'ьи', 'хф', 'щф'
    ]
    l = []
    for i in popular_big:
        for j in our_big:
            l.append((i, j))


    jv = []
    for j in l:
        for v in l:
            decrypted = decrypt(j[0]) - decrypt(v[0])
            encrypted = decrypt(j[1]) - decrypt(v[1])
            b = decrypt(j[1]) - a * decrypt(j[0])
            jv.append((a, b))
    print(jv)



func1()