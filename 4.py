text = input("Введите строку: ")
key = int(input("Введите ключ: "))
print(text, key)
text_ = list(text)
text_final = list()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_full = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

for i in range(len(text)):
    if text_[i].lower() in alphabet:
        a = alphabet_full.index(text_[i].lower())
        print(alphabet_full[a+key])
        text_[i] = alphabet_full[a+key]
#        print(text_[i], '->', alphabet_full[a+key])

text_final = ''.join(text_)
print(text)
print(text_final)