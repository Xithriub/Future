shoplist=['Яблоки','Манго','Морковь','Бананы']
print('Я должен сделать',len(shoplist),'покупки.')

print('Покупки:',end='^-^')
for item in shoplist:
    print(item,end=' ')
print('\nТакже нужно купить риса')
shoplist.append('Рис')
print('Теперь мой список покупок таков:',shoplist)
print('ОТсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный спиок выглядит вот так:',shoplist)

print('Первое что мне нужно купить, это', shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('Я купил',olditem)
print('Теперь мой список покупок таков:', shoplist)
print('\nБлин я забыл купить колу и чипсы^-^')
shoplist.append('Кола')# Добавляем новый товар в конец списка

shoplist.append('Чипсы')# Добавляем новый товар в конец спика после Колы

print('Теперь мой список таков:',shoplist)
toy=shoplist[0]
toi=shoplist[1]
del shoplist[0];del shoplist[1]
print('Я купил =',toy,'и',toi)
print('Мне осталось купить:',shoplist)
print('А еще надо купить самое важное, а это картошка')
shoplist.append('Картошка')
wer=shoplist[0]
wir=shoplist[1]
del shoplist[0];shoplist[1]
print('Мой новый список товаров:',shoplist)








