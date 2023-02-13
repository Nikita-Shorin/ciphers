import string
up_alphabet = string.ascii_uppercase + " "
lower_alphabet = string.ascii_lowercase + " "


def input_data():
    word = input("Введите слово, которое хотите зашифровать/дешифровать\n")
    while True:
        key = (input("Введите ключ (4 числа через пробел)\n")).split()
        if len(key) == 4 and [key[i].isdigit() for i in (0, 1, 2, 3)]:
            return word, int(key[0]) % 27, int(key[1]) % 27, int(key[2]) % 27, int(key[3]) % 27


def encryption_decryption():
    while True:
        enter = input("Введите 1, если хотите зашифровать слово\nВведите 2, если хотите дешифровать слово\n")
        if enter == '1':
            return encryption()
        elif enter == '2':
            return decryption()


def decryption():
    word, alpha1, beta1, alpha2, beta2 = input_data()
    alpha, beta = 0, 0
    answer = ""
    for i in range(len(word)):
        alpha1, beta1, alpha2, beta2, alpha, beta = iteration_num(i, alpha1, beta1, alpha2, beta2, alpha, beta)
        if word[i].isupper():
            index = up_alphabet.index(word[i])
            if index - beta < 0:
                index += 27
            while (index - beta) % alpha != 0:
                index += 27
            answer += up_alphabet[((index - beta) // alpha) % 27]
        else:
            index = lower_alphabet.index(word[i])
            if index - beta < 0:
                index += 27
            while (index - beta) % alpha != 0:
                index += 27
            answer += lower_alphabet[((index - beta) // alpha) % 27]
    return answer


def encryption():
    word, alpha1, beta1, alpha2, beta2 = input_data()
    alpha, beta = 0, 0
    answer = ""
    for i in range(len(word)):
        alpha1, beta1, alpha2, beta2, alpha, beta = iteration_num(i, alpha1, beta1, alpha2, beta2, alpha, beta)
        if word[i].isupper():
            answer += up_alphabet[(alpha * up_alphabet.index(word[i]) + beta) % 27]
        else:
            answer += lower_alphabet[(alpha * lower_alphabet.index(word[i]) + beta) % 27]
    return answer


def iteration_num(i, alpha1, beta1, alpha2, beta2, alpha, beta):
    if i == 0:
        alpha, beta = alpha1, beta1
    if i == 1:
        alpha, beta = alpha2, beta2
    if i == 2:
        alpha, beta = alpha1 * alpha2, beta1 + beta2
    if i > 2:
        alpha1, alpha2, beta1, beta2 = alpha2, alpha, beta2, beta
        alpha, beta = alpha1 * alpha2, beta1 + beta2
    return alpha1, beta1, alpha2, beta2, alpha, beta


print(encryption_decryption())
