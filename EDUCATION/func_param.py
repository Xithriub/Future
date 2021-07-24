def printmax(a,b):
    if a>b:
        print(a,'>',b,'о повезло\nповезло')
    elif a==b:
        print(a,'=',b,'А и Б равны друг другу')
    elif a<b:
        print(b,'>',a,'Б больше чем А')
printmax(7,6)# прямая передача значений

x=9
y=9
printmax(x,y)

