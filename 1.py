#Задача 1. Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом - то же самое и так до тех пор, пока не получится однозначное число.
#Пример:
#545 -> 5
#12345 -> 6

input_ = input("Введите целое число: ")
print(type(input_))
while len(str(input_)) != 1:
        print(input_, '---', len(str(input_)))
        input_ = sum(int(number) for number in str(input_))
        print(input_)
print(f"Результат суммы цифр введенного числа {input_}")