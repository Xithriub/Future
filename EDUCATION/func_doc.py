def printMax(x,y):
    '''Выводит максимальное значение из двух чисел.

    Оба значения должны быть целыми числами,'''
    x=int(x) #конвертируем в целые числа
    y=int(y)

    if x>y:
        print(x,'наибольшее')
    else:
        print(y,'наибольшее')
printMax(3,5)
print(printMax.__doc__)