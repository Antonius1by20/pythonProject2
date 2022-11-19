#Задание №1
#Найти самое длинное слово в строке.
#Задание №2
#Преобразовать текст в список слов с удалением знаков препинания
a = ('я', 'иду', 'гулять')

b = ' '.join(a)
print(b)
d = list(a)
c = ' '.join(d)
print(d)
max_len = 0
max_word = ''
for word in (a):
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print('Самое длинное слово:', max_word)
print('Длина этого слова:', max_len)
