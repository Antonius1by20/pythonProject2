#Заполните один кортеж десятью случайными целыми числами от 0 до 5
#включительно. Также заполните второй кортеж числами от -5 до 0.
#Объедините два кортежа с помощью оператора +, создав тем самым третий
#кортеж. С помощью метода кортежа count() определите в нем количество
#нулей. Выведите на экран третий кортеж и количество нулей в нем.

import random
a = tuple(random.randint(0,5)
          for i in range(10))
b = tuple(random.randint(0,5)
          for i in range(10))
c = a + b
print('кортеж:',c)
d = c.count(0)
print('количество нулей:',d)


