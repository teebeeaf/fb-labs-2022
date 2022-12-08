#Task 0 completed

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

#Task 1 completed, helper functions


def convert_bigram(text: str, bool = 0):
    symbols = list()  # Creating a symbols dictionary
    i = 0  # Creating an iterator 'i'
    crypted = [] # Creating a crypt
    while i <= len(text) - 2:  # Using a while cycle
        x = alphabet.find(text[i]) * len(alphabet) + alphabet.find(text[i + 1])
        symbols.append(x)
        crypted.append(x)
        i += 2

    if bool:
        return crypted

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
    counter = 0
    if gcd == 1:
        possible_a.append(linear_euclid(a,mod))
        counter += 1
    else:
        if b % gcd == 0:
            a1 = a // gcd
            b1 = b // gcd
            n1 = mod // gcd
            x0 = linear_euclid(a1, n1)
            x0 = x0 * b1 % n1
            for i in range(gcd):
                possible_a.append(x0 + i * n1)
                counter += 1
    return possible_a


# print(linear_gcd(35,5))
#
# print(linear_euclid(608,961))
#
# print(euclid_rev(608,961))

# def linear_equations(a, b, n):
#         if a

# print(linear_equations(31,93,961))


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


#Task 2 completed, most common bigrams
with open('finaltext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

b = list(sorted(bigrams(text).items()))
b.sort(key=lambda x: -x[1])
print(b[:10])

def get_all_the_keys():
    # get al the managable keys
    popular_big = [
        "ст", "но", "то", "на", "ен"
    ]
    our_big = [
        'уф', 'иж', 'ьи', 'хф', 'щф'
    ]
    # our_big = [
    #     'шф', 'уй', 'ду', 'цф', 'кч'
    # ]
    l = []
    for i in popular_big:
        for word1 in our_big:
            l.append((i, word1))

    mod = 961  # 31 * 31

    word1_word2 = []
    for word1 in l:
        for word2 in l:

            a_x, b_x = decrypt(word1[0]), decrypt(word1[1])  # for b calculation
            a = decrypt(word1[0]) - decrypt(word2[0])  # X* - X** (a)
            b = decrypt(word1[1]) - decrypt(word2[1])  # Y* - Y** (b)

            if a == 0:
                continue

            possible_a = linear_equations(a, b, mod)

            for i in possible_a:
                if linear_gcd(a, 31) != -1:
                    possible_b = (b_x - i * a_x) % mod
                    word1_word2.append((i, possible_b))
                else:
                    continue

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

    word1_word2 = list(set(word1_word2))
    print(word1_word2)
    return word1_word2

keys = get_all_the_keys()

get_crypt = convert_bigram(text)

print(len(keys))
for i in keys:
    a, b = i[0], i[1]
    decrypted = ''
    for i in get_crypt:
        a_rev = linear_euclid(a, 961)
        deci_x = ((i - b) * a_rev) % 961
        word = str(alphabet[deci_x // 31]) + str(alphabet[deci_x % 31])
        decrypted += word
    print(f'Keys: {a}, {b},( {a_rev}')
    print(decrypted)
    # with open('bob.txt', 'a', encoding='utf-8') as file:
    #     file.write(f'Keys: {a}, {b},( {a_rev}\n')
    #     file.write(f'{decrypted}\n')




