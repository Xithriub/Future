print('Простое присваивание')
shoplist=['яблоки','манго','морковь','бананы']
mylist=shoplist


del shoplist[0]
print('shoplist:', shoplist)
print('mylist:', mylist)

# Обратите внимание что и shoplist, и mylist выводят один и тот же список 
# без пункта 'яблоко' подтверждая тем самым что они указывают на один объект

print('Копирование при помощи полной вырезки ')
mylist=shoplist[:]
del mylist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание что списки теперь разные