from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
len1 = int(input('Какой длины должен быть пароль? '))
digits1 = input('Включать ли в пароль цифры от 0 до 9? (да/нет) ')
uppercase1 = input('Включать ли в пароль прописные буквы? (да/нет) ')
lowercase1 = input('Включать ли в пароль строчные буквы? (да/нет) ')
punctuation1 = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (да/нет) ')
exceptions1 = input('Исключать ли неоднозначные символы "il1Lo0O"? (да/нет) ')
if digits1 == 'да':
    chars += digits
if uppercase1 == 'да':
    chars += uppercase_letters
if lowercase1 == 'да':
    chars += lowercase_letters
if punctuation1 == 'да':
    chars += punctuation
if exceptions1.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, char):
    password = ''
    for j in range(length):
        password += choice(char)
    print(password)


for _ in range(quantity):
    generate_password(len1, chars)
