#Создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент.
import random
a = tuple(random.randint(1,10)
          for i in range(10))
print(a)
print('max', max(a), 'min', min(a))