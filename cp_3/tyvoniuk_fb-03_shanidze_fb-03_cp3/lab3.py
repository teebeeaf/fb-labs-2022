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

def euclid_rev(a: int, b: int): #player reverse func
    return pow(a, -1, b)

def linear_gcd(a: int, b: int): #returns gcd of nums
    rest = a % b
    while rest != 0:
        a = b
        b = rest
        rest = a - (b * int(a / b))
    return b

def linear_euclid(a: int, b: int): # returns inverse with mod
    a = a%b
    mod = b
    if a == 0:
        return 0
    nodes = [1, 0]
    while b != 0:
        nodes = [nodes[1], nodes[0] - (a // b) * nodes[1]]
        a, b = b, a % b
    return nodes[0] % mod

def linear_equations(a: int, b: int, mod: int): #returns an (a) of possible key
    possible_a = []
    gcd = linear_gcd(a % mod, mod)
    print(gcd)
    if gcd == 1:
        possible_a.append(linear_euclid(a,mod))
    else:
        if b % gcd == 0:
            a1 = a // gcd
            b1 = b // gcd
            n1 = mod // gcd
            x0 = linear_euclid(a1, n1)
            x0 = x0 * b1 % n1
            for i in range(gcd):
                possible_a.append(x0 + i * n1)
    return possible_a


print(linear_gcd(35,5))

print(linear_euclid(608,961))

print(euclid_rev(608,961))

# def linear_equations(a, b, n):
#         if a

print(linear_equations(31,93,961))


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
        for word1 in our_big:
            l.append((i, word1))

    mod = 961 # 31 * 31

    word1_word2 = []
    for word1 in l:
        for word2 in l:

            a_x, b_x = decrypt(word1[0]), decrypt(word1[1]) #for b calculation
            a = decrypt(word1[0]) - decrypt(word2[0]) #X* - X** (a)
            b = decrypt(word1[1]) - decrypt(word2[1]) #Y* - Y** (b)

            if a == 0 or b == 0:
                continue

            possible_a = linear_equations(a, b, mod)

            for i in possible_a:
                possible_b = (b_x - i * a_x) % mod
                word1_word2.append((i, possible_b))
            #
            #
            #
            # gcd, inverse = hernya[0] % mod, hernya[1]
            # print(gcd)
            # result = []
            # if gcd == 1:
            #     result.append(inverse % mod)
            # else:
            #     if gcd == 0 or b % gcd != 0:
            #         continue
            #     else:
            #         a1 = a // gcd
            #         b1 = b // gcd
            #         n1 = mod // gcd
            #         res = euclid_perdic(a1, n1)
            #         print(str(res[1]) + ' ' + str(a1) + ' ' + str(n1))
            #         x0 = (res[1]*b1) % n1
            #         i = 0
            #         while i < gcd:
            #             result.append(x0)
            #             x0 += n1
            #             i += 1
            # i = 0
            # while i < len(result):
            #     result[i] = result[i], (decrypt(word1[1]) - decrypt(word1[0]) * result[i]) % mod
            #     i += 1

    print(word1_word2)

#Task 2 completed, most common bigrams
with open('finaltext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

b = list(sorted(bigrams(text).items()))
b.sort(key=lambda x: -x[1])
print(b[:10])

print(func1())

