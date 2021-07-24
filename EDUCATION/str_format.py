#age=26

#name='Swaroop'

#print('Возраст {}--{} лет.'.format(name,age))

#print('Почему {} забваляется с этим Python?'.format(name))


#i=5;print(i);i=i+1;print(i)

#s='''Это многострочная строка.\

#Это вторая ее строка.'''

#print(s)

#Q=[12,34]
#for i in range(Q):
    #([1,2,3]).append(4)
#print([1,2,3])


poka=True
while poka:
    vvod=int(input('Введите пароль:'))
    vvo=int(input('Введите снова пароль:'))
    if vvod==vvo:
        print('Вы успешно вошли\nв систему')
        break
    elif vvod!=vvo:
        print('Вы не вошли\nв систему')
else:
    print('Цикл заверешен')
print('Завершение программы')


    