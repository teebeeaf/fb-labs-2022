#Task 0 completed

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

#Task 1 completed, helper functions


def convert_bigram(text: str):
    symbols = list()  # Creating a symbols dictionary
    i = 0  # Creating an iterator 'i'
    while i < len(text) - 2:  # Using a while cycle
        x = alphabet.find(text[i]) * len(alphabet) + alphabet.find(text[i + 1])
        symbols.append(x)
        i += 2
    return symbols

# def linear_equations(a, b, n):
#         if a



def euclid_perdic(a: int, b: int):
    while
    div = b // a
    rest = b % a

    return y1 - (b // a) * x1


def decrypt(text):
    return alphabet.find(text[0]) * 31 + alphabet.find(text[1])


def bigrams(text: str) -> dict:
    symbols = dict()  # Creating a symbols dictionary
    i = 0  # Creating an iterator 'i'
    while i < len(text) - 2:  # Using a while cycle
        bigram = f'{text[i]}{text[i + 1]}'  # Creating a bigram
        if bigram not in symbols:  # Looking for it in symbols dictionary
            symbols[bigram] = 1  # Adding a new one
        else:  # else
            symbols[bigram] += 1  # Raise the old one
        i += 2  # Raise an iterator

    return symbols  # Returning our dictionary


def func1():
    #get al the managable keys

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
            print(str(j) + " j " + str(v) + " v")
            mod = 961
            a_x, b_x = decrypt(j[0]), decrypt(j[1])
            a = decrypt(j[0]) - decrypt(v[0]) #X* - X** (a)
            b = decrypt(j[1]) - decrypt(v[1]) #Y* - Y** (b)
            hernya = euclid_perdic(a, mod)
            gcd, inverse = hernya[0] % mod, hernya[1]
            print(gcd)
            result = []
            if gcd == 1:
                result.append(inverse % mod)
            else:
                if gcd == 0 or b % gcd != 0:
                    continue
                else:
                    a1 = a // gcd
                    b1 = b // gcd
                    n1 = mod // gcd
                    res = euclid_perdic(a1, n1)
                    print(str(res[1]) + ' ' + str(a1) + ' ' + str(n1))
                    x0 = (res[1]*b1) % n1
                    i = 0
                    while i < gcd:
                        result.append(x0)
                        x0 += n1
                        i += 1
            i = 0
            while i < len(result):
                result[i] = result[i], (decrypt(j[1]) - decrypt(j[0])*result[i]) % mod
                i += 1
            jv.append(result)

    print(jv)

#Task 2 completed, most common bigrams
with open('finaltext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

b = list(sorted(bigrams(text).items()))
b.sort(key=lambda x: -x[1])
print(b[:10])

# print(func1())

print(euclid_perdic(12, 961))
print(euclid_perdic(58, 961))
print(euclid_perdic(301, 961))
print(euclid_perdic(452, 961))
