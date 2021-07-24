def perimetr():
    dlina=float(input('Введите сторону:'))
    p=dlina+otvet
    return p
storony=int(input('Сколько сторон у многоугольника?:'))
otvet=1
if storony<3:
    print('Ошибка! У многоугольника больше 2х сторон.')
else:
    for i in range(storony):
        otvet=perimetr()
    print('Периметр',storony,'-угольника равен',otvet)
