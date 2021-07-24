#1
#vvod=str(input('Введите букву:'))
#print(vvod.upper())

#2
#def maximum(x,y):
    #if x>y:
        #return 'X больше чем Y'
    #elif x==y:
        #return 'Числа равны'
    #elif y>x:
        #return 'Y больше чем X'
#x=int(input('Введите число:'))
#y=int(input('Введите число:'))
#print(maximum(x, y))

#3
#days = {'Понедельник':1, 'Вторник':2, 'Среда':3,'Четврег':4, 'Пятница':5, 'Суббота':6, 'Воскресенье':7}
#d=int(input('Введите номер:'))
#for k,v in days.items():
    #if v==d:
        #print(k)

tovar=int(input('Сколько всего товаров?:'))
naimenovanie=[]
tsena=[]
kolvo=[]
itogo=0
for i in range(tovar):
    naimenovanie.append(str(input('Товар:')))
    tsena.append(float(input('Цена:')))
    kolvo.append(float(input('Количество:')))
# открываем файл в Check.txt для записи
f=open('Check.txt','w')
# вписываем в файл заголовки столбцов чека
print('Наименование', 'Цена(сомов)', 'Количество(шт)', 'Стоимость (сомов)', sep='\t', file=f)
# в цикле заполняем столбцы и рассчитываем стоимость
for i in range(tovar):
    print(naimenovanie[i],tsena[i], kolvo[i], tsena[i]*kolvo[i],sep='\t\t', file=f)
    # накапливаем итоговую сумму
    itogo=itogo+tsena[i]*kolvo[i]
# выводим линию
print('-'*20,file=f)
# выводим итоговую сумму
print('ИТОГО:',round(itogo,2),'сомов к оплате',file=f)
# закрываем файл
f.close()





