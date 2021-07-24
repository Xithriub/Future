class Operation:#название класса
    def __init__(self,plus,pri,otch,pris,spis):
        self.spis=[]
        self.plus=plus
        self.pri=pri
        self.otch=otch
        self.pris=pris
    def pribavit(self):
        return self.plus+self.pri
    def minus(self):
        return self.otch-self.pris
    def delenie(self):
        dele=self.plus/self.pri
        return'():'.format(dele)
    def umnozhenie(self):
        umno=self.otch*self.pris
        return'():'.format(umno)
    def stepen(self):
        step=(self.plus+self.pri)**2
        return'():'.format(step)
    def znach(self):
        return self.plus%self.pri==0
    def diskrim(self):
        dis=(plus**2)-4*self.pri*self.otch
        return '():'.format(dis)
plus=int(input('Введите число:'))
pri=int(input('Введите число:'))




