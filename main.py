def rle(input_string):
    result = []
    count = 1

    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            count += 1
        else:
            result.append((count, input_string[i]))
            count = 0

    # Обработка последнего элемента
    if count > 0:
        result.append((count, input_string[-1]))

    return ''.join([str(x[0]) + x[1] for x in result])


# Примеры использования
print("aaabbbbccccc ->", rle("aaabbbbccccc"))  # Результат: 3a4b5c
print("asssdddsssddd ->", rle("asssdddsssddd"))  # Результат: 1a3s3d3s3d
print("abcba ->", rle("abcba"))  # Результат: 1a1b1c1b1a
