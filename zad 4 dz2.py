a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
summa1 = 0
summa2 = 0
for i in a:
    summa1 +=i
for j in b:
    summa2 +=j
print(summa1, 'min a =', min(a))
print(summa2, 'min b =', min(b))
