Задача 1. Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом - то же самое и так до тех пор, пока не получится однозначное число.
Пример:
545 -> 5
12345 -> 6

Задача 2. Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0, Количество вложенных списков - количество рядов. Пользователь вводит сколько билетов ему требуется. Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом). Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд). Ели таких мест нет, то вывести False
Пример:
[[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
[[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False

Задача 3. Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
Пример:
aaabbbbccccc -> 3a4b5c
asssdddsssddd -> 1a3s3d3s3d
abcba -> 1a1b1c1b1a

Задача 4. Шифр Цезаря. Пользователь вводит строку и ключ шифра, программа должна вывести зашифрованную строку (со сдвигом по ключу). Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются.
Пример:
Dog, 2 -> Fqi
Zak zak, 3 -> Cdn cdn
Python is the BEST, 5 -> Udymts nx ymj GJXY
