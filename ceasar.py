flag = 0
blag = 0
print('Добро пожаловать в программу шифр Цезаря!')
while True:
    a = input('Будем шифровать или дешифровать? (шифр/дешифр)\n')
    if a == 'шифр':
        break
    elif a == 'дешифр':
        blag += 1
        break
    else:
        print('Некорректный ввод')
while True:
    lan = input('Выберете язык алфавита (ру/анг)\n')
    if lan == 'ру':
        break
    elif lan == 'анг':
        flag += 1
        break
    else:
        print('Некорректный ввод')

step = int(input('Укажите шаг сдвига шифра\n'))
en_alphabet1 = [chr(i) for i in range(65, 91)]
en_alphabet2 = [chr(j) for j in range(97, 123)]
ru_alphabet1 = [chr(i) for i in range(1040, 1072)]
ru_alphabet2 = [chr(i) for i in range(1072, 1104)]
marks = [chr(i) for i in range(33, 48)]


def cipher_ru():
    print('Шифровальный модуль запущен.')
    s = input('Введите фразу\n')
    for i in range(len(s)):
        if s[i] in marks or s[i] == ' ':
            print(s[i], end='')
        elif s[i] in ru_alphabet1:
            if ord(s[i]) + step > ord('Я'):
                print(chr(ord(s[i]) + step - 33), end='')
            else:
                print(chr(ord(s[i]) + step), end='')
        elif s[i] in ru_alphabet2:
            if ord(s[i]) + step > ord('я'):
                print(chr(ord(s[i]) + step - 33), end='')
            else:
                print(chr(ord(s[i]) + step), end='')


def cipher_en():
    print('Шифровальный модуль запущен.')
    s = input('Введите фразу\n')
    for i in range(len(s)):
        if s[i] in marks or s[i] == ' ':
            print(s[i], end='')
        elif s[i] in en_alphabet1:
            if ord(s[i]) + step > ord('Z'):
                print(chr(ord(s[i]) + step - 26), end='')
            else:
                print(chr(ord(s[i]) + step), end='')
        elif s[i] in en_alphabet2:
            if ord(s[i]) + step > ord('z'):
                print(chr(ord(s[i]) + step - 26), end='')
            else:
                print(chr(ord(s[i]) + step), end='')


def decipher_ru():
    print('Дешифровальный модуль запущен.')
    s = input('Введите фразу\n')
    for i in range(len(s)):
        if s[i] in marks or s[i] == ' ':
            print(s[i], end='')
        if s[i] in ru_alphabet1:
            if ord(s[i]) - step < ord('А'):
                print(chr(33 + ord(s[i]) - step), end='')
            else:
                print(chr(ord(s[i]) - step), end='')
        elif s[i] in ru_alphabet2:
            if ord(s[i]) - step < ord('а'):
                print(chr(32 + ord(s[i]) - step), end='')
            else:
                print(chr(ord(s[i]) - step), end='')


def decipher_en():
    print('Дешифровальный модуль запущен.')
    s = input('Введите фразу\n')
    for i in range(len(s)):
        if s[i] in marks or s[i] == ' ':
            print(s[i], end='')
        if s[i] in en_alphabet1:
            if ord(s[i]) - step < ord('A'):
                print(chr(26 + ord(s[i]) - step), end='')
            else:
                print(chr(ord(s[i]) - step), end='')
        elif s[i] in en_alphabet2:
            if ord(s[i]) - step < ord('a'):
                print(chr(26 + ord(s[i]) - step), end='')
            else:
                print(chr(ord(s[i]) - step), end='')


if blag == 1 and flag == 0:
    decipher_ru()
elif blag == 0 and flag == 0:
    cipher_ru()
elif blag == 0 and flag == 1:
    cipher_en()
elif blag == 1 and flag == 1:
    decipher_en()
