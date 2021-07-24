def maximum(x,y):
    if x>y:
        return 'X больше чем Y'
    elif x==y:
        return 'Числа равны'
    elif y>x:
        return 'Y больше чем X'
x=int(input('Введите число:'))
y=int(input('Введите число:'))
print(maximum(x, y))