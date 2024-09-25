def check_num(numm):
    if numm <= 1:
        return False
    for i in range(2, numm):
        if numm % i == 0:
            return False
    return True

while num := input("Введите число: "):
    numm = int(num)
    print(numm, "->", check_num(numm))
    print("Для выхода нажмите Enter")
