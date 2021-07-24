while True:
    s=input('Введите что-нибудь:')
    if s=='Выход':
        break
    if len(s)<3 and len(s)<4:
        print('Слишком мало')
        continue
    print('Введеная строка достаточной длины')
