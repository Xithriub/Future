class Robot:

    '''Представляет робото с именем.'''

    #Переменная класса, содержащая количество роботов

    population=0


    def __init__(self,name):

        '''Инициализация данных.'''

        self.name=name

        print('(Инициализация {0})'.format(self.name)) 


        #При создании этой личности, робот добавляется

        #к переменной 'population'

        Robot.population+=1

    def __del__(self):

        '''Я умираю.'''

        print('{0} уничтожается!'.format(self.name))


        Robot.population-=1


        if Robot.population==0:

            print('{0} был последним'.format(self.name))

        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population ))

    def sayHi(self):
            '''Приветствие робота

            да они это могут'''

            print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
        
    def howmany():
            '''Выводит численность роботов'''
            print('У нас {0:d} роботов.'.format(Robot.population))

    howmany=staticmethod(howmany)

    
droid1=Robot('R2-D2')
droid1.sayHi()
Robot.howmany()

droid2=Robot('C-3PO')
droid2.sayHi()
Robot.howmany()

print("\nЗдесь роботы могут проделать какую-то работу\n")

print("Роботы закончили свою работу. Давайте уничтожим их")

del droid1

del droid2

Robot.howmany()
