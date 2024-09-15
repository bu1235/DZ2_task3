#Задача 3. Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
#Пример:
#aaabbbbccccc -> 3a4b5c
#asssdddsssddd -> 1a3s3d3s3d
#abcba -> 1a1b1c1b1a


a = input("Введите строку: ")
print(a)
result = []
count = 1
for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count = count + 1
        else:
            result.append((count, a[i]))
            count = 1
#        print(result)
if count > 0:
        result.append((count, a[-1]))
print(result)
final_result = ''.join([str(x[0]) + x[1] for x in result])
print(final_result)