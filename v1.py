import string
up_alphabet = string.ascii_uppercase
lower_alphabet = string.ascii_lowercase


def encryption():
    word, key = input_data()
    answer = ""
    up_key = key.upper()
    lower_key = key.lower()
    for letter in word:
        if letter.isupper():
            index = up_alphabet.index(letter)
            answer += up_key[index]
        else:
            index = lower_alphabet.index(letter)
            answer += lower_key[index]
    return answer


def decryption():
    word, key = input_data()
    answer = ""
    up_key = key.upper()
    lower_key = key.lower()
    for letter in word:
        if key.isupper():
            index = up_key.index(letter)
            answer += up_alphabet[index]
        else:
            index = lower_key.index(letter)
            answer += lower_alphabet[index]
    return answer


def encryption_decryption():
    while True:
        enter = input("Введите 1, если хотите зашифровать слово\nВведите 2, если хотите дешифровать слово\n")
        if enter == '1':
            return encryption()
        elif enter == '2':
            return decryption()


def input_data():
    word = input("Введите слово, которое хотите зашифровать/дешифровать\n")
    while True:
        key = input("Введите ключ (26 символов английского алфавита)\n")
        if len(key) == 26:
            return word, key


print(encryption_decryption())
