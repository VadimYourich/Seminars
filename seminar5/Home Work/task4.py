# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(text):
    res = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            res += str(count) + text[i - 1]
            count = 1
    res += str(count) + text[i]
    return res

def decode(text):
    res = ''
    digit = ''
    for i in range(0, len(text)):
        if text[i].isdigit():
            digit += text[i]
        else:
            res += int(digit) * text[i]
            digit = ''
    return res

if __name__ == '__main__':
    with open('input.txt') as file:
        text = file.readline().strip()
    encode_text = encode(text)
    print(encode_text)
    with open('encode_output.txt', 'w') as file:
        file.write(encode_text)
    decode_text = decode(encode_text)
    with open('decode_output.txt', 'w') as file:
        file.write(decode_text)