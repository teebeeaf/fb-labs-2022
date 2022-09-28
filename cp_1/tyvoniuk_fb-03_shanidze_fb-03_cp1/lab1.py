from pprint import pprint
import math

# Task 0

# Function to read metodichka
def read_carefully():
    return "Done"

# Function to solve the first task
def task0():
    return read_carefully()


# Task 1

# Function to count a frequency of one letter
def one_symbol(text: str) -> dict:
    symbols = dict() # Creating a dictionary
    for i in text: # Using a cycle
        if i not in symbols: # check if our symbol is already in symbols dictionary
            symbols[i] = 1 # Adding a symbol if it is absent
        else: # else
            symbols[i] += 1 # Raise this one if it already exists

    symbols_sort = {
        list(symbols.keys())[i]: sorted(symbols.values())[i] for i in range(len(list(symbols.keys())) - 1, -1, -1)
    } # Sorting dictionary by value

    return symbols_sort # Returning our dictionary

# Function to count a frequency of bigrams
def bigrams(text: str, intersection: bool) -> dict:
    symbols = dict() # Creating a symbols dictionary
    i = 0 # Creating an iterator 'i'
    while i < len(text) - 1: # Using a while cycle
        bigram = f'{text[i]}{text[i + 1]}' # Creating a bigram
        if bigram not in symbols: # Looking for it in symbols dictionary
            symbols[bigram] = 1 # Adding a new one
        else: # else
            symbols[bigram] += 1 # Raise the old one
        i += 1 # Raise an iterator
        if not intersection: # If we need bigrams without intersection
            i += 1 # Raise it again

    return symbols # Returning our dictionary

# Function to build a matrix for bigrams
def beauty_bigrams(bigram: dict) -> str:
    alph = 'абвгдежзийклмнопрстуфхцчшщыьэюя ' # It is our alphabet
    beauty = ['\\'] # Creating a list with our matrix
    sym_count = len(alph) # Checking the number of letters in the alphabet
    for i in range(sym_count - 1): # using for cycle
        beauty.append(f'    {alph[i]}') # Appending a letter to our list
    beauty.append('\n') # creating a new line
    for i in range(sym_count - 1): # Using a for cycle
        beauty.append(alph[i]) # Appending a letter from alphabet to our list
        for j in range(sym_count - 1): # Using for cycle again
            try: # Checking if bigram exists
                temp = str(bigram[f'{alph[j]}{alph[i]}']) # Creating a bigram
                beauty.append(f'{" " * (5 - len(temp))}{temp}') # Appending created bigram to our list
            except KeyError: # if not
                beauty.append('    0') # Appending zero to our list
        beauty.append('\n') # Creating a new line
    return " ".join(beauty) # Returning it in the string type

# Function to find result of H1
def h1_count(symbol_dict: dict, l: int, space: bool) -> float:
    answer = 0 # Creating an answer variable
    for i in symbol_dict.keys(): # Using a cycle for
        if not space and i == ' ': # If we need answer without spaces
            continue # continue
        answer -= (symbol_dict[i] / l) * math.log(symbol_dict[i] / l, 2) # using our super formula
    return answer # returning answer (H)

# Function to find result of H2
def h2_count(bygram_dict: dict, l: int, space: bool) -> float:
    answer = 0 # Creating an answer variable
    for i in bygram_dict.keys(): # Using a cycle for
        if not space and " " in i: # If we need answer without spaces
            continue # continue
        answer -= (bygram_dict[i] / l) * math.log(bygram_dict[i] / l, 2) # using our super formula
    return answer / 2 # returning answer (H)

# Task 3

# Function to find result of R
def count_R(e: float, number_alph: int) -> float:
    h_0 = math.log(number_alph, 2) # using our super formula
    return 1 - (e / h_0) # returning an answer (H)!!!



if __name__ == "__main__":
    print(task0())

    symbol_count = 32
    bigram_count = 32 * 32

    with open('finaltext.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    one_symbol_dict = one_symbol(text)
    h1_s = round(h1_count(one_symbol_dict, len(text), True), 3)
    print(f"H1 (spaces): {h1_s}")


    one_symbol_dict = one_symbol(text)
    h1_ = round(h1_count(one_symbol_dict, len(text), False), 3)
    print(f"H1 (NO spaces): {h1_}")


    ok = input('Do u want to check bigrams (Click "Enter" if no)\n')

    bigrams_dict = bigrams(text, True)
    h2_i_s = round(h2_count(bigrams_dict, len(text), True), 3)
    print(f"H2 (intersection, spaces): {h2_i_s}")
    if ok:
        print(beauty_bigrams(bigrams_dict))

    bigrams_dict = bigrams(text, True)
    h2_i = round(h2_count(bigrams_dict, len(text), False), 3)
    print(f"H2 (intersection, NO spaces): {h2_i}")
    if ok:
        print(beauty_bigrams(bigrams_dict))

    bigrams_dict = bigrams(text, False)
    h2_s = round(h2_count(bigrams_dict, len(text), True), 3)
    print(f"H2 (NO intersection, spaces): {h2_s}")
    if ok:
        print(beauty_bigrams(bigrams_dict))


    bigrams_dict = bigrams(text, False)
    h2_ = round(h2_count(bigrams_dict, len(text), False), 3)
    print(f"H2 (NO intersection, NO spaces): {h2_}")
    if ok:
        print(beauty_bigrams(bigrams_dict))


    print(f"R: {round(count_R(h2_, symbol_count), 3)}")