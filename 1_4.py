def valid_name(name):
    valid_chars = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in name:
        if char.lower() not in valid_chars:
            return False
    return True

def valid_surname(surname):
    valid_chars = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in surname:
        if char.lower() not in valid_chars:
            return False
    return True

def valid_age(age):
    if not age.isdigit():
            return False
    else:
        if not 17 < int(age) < 61:
            return False
    return True

def upper_letter(word):
    words = word.split()
    upper_words = []
    for w in words:
        upper_words.append(w[0].upper() + w[1:])
    return ' '.join(upper_words)

def valid_id(id_):
    if not id_.isdigit():
            return False
    return True

human_dict = {}
while True:
    line = input("Введите имя, фамилию, возраст и ID: ")
    if len(line) == 0:
        break
    name, surname, age, id_ = line.split()
    f = 0
    if not valid_name(name):
        print("Ваше имя содержит недопустимые символы.")
        f = 1
    if not valid_surname(surname):
        print("Ваша фамилия содержит недопустимые символы.")
        f = 1
    if not valid_age(age):
        print("Ваш возраст содержит недопустимые символы или не подходит.")
        f = 1
    if not valid_id(id_):
        print("Ваш ID содержит недопустимые символы.")
        f = 1
    print("Flag is: ", f)
    if f == 0:
        if not id_ in human_dict:
            if len(id_) < 8:
                j = 8 - len(id_)
                for i in range(j):
                    id_ = '0' + id_
            human_dict[id_] = (upper_letter(name), upper_letter(surname), age)
            print("Human not in dict, added: ", human_dict)
        else:
            print("Your ID il already in dict: ", human_dict)
            print("Ошибка ввода, повторите ввод.")
    else:
        print("Ошибка ввода, повторите ввод.")

print(human_dict)

def dict_print(human_dict):
    for id_ in human_dict:
        print(id_, ":", human_dict[id_])

dict_print(human_dict)

