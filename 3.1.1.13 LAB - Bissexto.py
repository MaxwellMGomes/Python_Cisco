'''
se o número do ano não for divisível por quatro, é um ano comum ;
caso contrário, se o número do ano não for divisível por 100, é um ano bissexto ;
caso contrário, se o número do ano não for divisível por 400, é um ano comum ;
caso contrário, é um ano bissexto .

Ano Caledário Gregoriano ==> 1582

'''

while True:
    ano = int(input("Insira um ano: "))
    bs = ''
    if ano == 0 : break
    if ano < 1582 : bs = 'fora do calendário Gregoriano'
    elif ano % 4 != 0 : bs = 'comum'
    else:
        if ano % 100 != 0: bs = 'bissexto'
        elif ano % 400 != 0 : bs = 'comum'
        else : bs = 'bissexto'

    print(f"O ano {ano} é um ano {bs}.")