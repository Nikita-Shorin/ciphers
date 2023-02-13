import string
up_alphabet = string.ascii_uppercase
lower_alphabet = string.ascii_lowercase


def input_data():
    word = input("Введите слово, которое хотите зашифровать/дешифровать\n")
    while True:
        key = (input("Введите ключ (2 числа через пробел)\n")).split()
        if len(key) == 2 and key[0].isdigit() and key[1].isdigit():
            return word, int(key[0]) % 26, int(key[1]) % 26


def encryption_decryption():
    while True:
        enter = input("Введите 1, если хотите зашифровать слово\nВведите 2, если хотите дешифровать слово\n")
        if enter == '1':
            return encryption()
        elif enter == '2':
            return decryption()


def decryption():
    word, alpha, beta = input_data()
    answer = ""
    for letter in word:
        if letter.isupper():
            index = up_alphabet.index(letter)
            if index - beta < 0:
                index += 26
            while (index - beta) % alpha != 0:
                index += 26
            answer += up_alphabet[((index - beta) // alpha) % 26]
        else:
            index = lower_alphabet.index(letter)
            if index - beta < 0:
                index += 26
            while (index - beta) % alpha != 0:
                index += 26
            answer += lower_alphabet[((index - beta) // alpha) % 26]
    return answer


def encryption():
    word, alpha, beta = input_data()
    answer = ""
    for letter in word:
        if letter.isupper():
            answer += up_alphabet[(alpha * up_alphabet.index(letter) + beta) % 26]
        else:
            answer += lower_alphabet[(alpha * lower_alphabet.index(letter) + beta) % 26]
    return answer


print(encryption_decryption())
