import string
lower_alphabet = string.ascii_lowercase
frequency = {'e': 12.702, 't': 9.056, 'a': 8.167, 'o': 7.507, 'i': 6.966, 'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253, 'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.361, 'f': 2.228, 'g': 2.015, 'y': 1.974, 'p': 1.929, 'b': 1.492, 'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095, 'z': 0.074}
text = input()
min_summa, min_alpha, min_beta = 1_000_000_000, 0, 0
summa = 0
frequency_for_text = {k: text.count(k) / len(text) * 100 for k in lower_alphabet}

for alpha in (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):
    for beta in range(0, 26):
        for letter in text:
            index = lower_alphabet.index(letter)
            if index - beta < 0:
                index += 26
            while (index - beta) % alpha != 0:
                index += 26
            summa += frequency_for_text[letter] * frequency[lower_alphabet[((index - beta) // alpha) % 26]]
    if summa < min_summa:
        min_summa = summa
        min_alpha = alpha
        min_beta = beta
        print(alpha, beta)
    summa = 0




answer = ""
for letter in text:
    if letter == " ":
        answer += " "
    index = lower_alphabet.index(letter)
    new_index = (min_alpha * index + min_beta) % 26
    answer += lower_alphabet[new_index]
print(min_alpha, min_beta, min_summa, answer)