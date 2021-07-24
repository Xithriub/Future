#import random
#fos=random.randint(1,10)
#vvod=0
#chan=3
#while (vvod!=fos)and(chan!=0):
    #print('Осталось попыток:',chan)
    #vvod=int(input('Введите число:'))
    #chan=-1
    #if chan==0:
        #print('К сожалению у вас не осталось попыток =')
        #break
    #else:
        #print('Вы угадали! Это было число =',fos)


def rectangle(x,y,t,u,o,p):
    return x*y
    return t%u
    return (o*p)**2
x=int(input('Введите число х'))
y=int(input('Введите число y:'))
t=int(input('Введите число t:'))
u=int(input('Введите число u:'))
o=int(input('Введите число о'))
p=int(input('Введите число р:'))
print(rectangle(x, y, t, u, o, p))


class unical():
    def __init___(self,name,obj):
        self.name=name
        self.obj=obj
    def tiser(self):
        