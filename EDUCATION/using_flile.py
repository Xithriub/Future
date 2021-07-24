poem='''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

f=open('poem.txt','w')# открываем для записи (for writing)
f.write(poem)# записываем текст в файл
f.close()# закрываем файл


f=open('poem.txt')# если не указан режим по умолчанию подразумевается
                  # режим чтения (reading)
while True:
    line=f.readline()
    if len(line)==0: # нулевая длина обозначает конец файла
        break
    print(line, end='')

f.close()