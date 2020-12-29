
def Lista_Chapeu():
    hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

    # Step 1: write a line of code that prompts the user
    # to replace the middle number with an integer number entered by the user.

    print ('\nLista original : ',hatList)

    hatList[2] = int(input('Digite o número a se substituido na lista: '))

    print('Lista alterada :', hatList)
    print('Tamando original da lista é : ',len(hatList))

    # Step 2: write a line of code here that removes the last element from the list.

    del hatList[-1]
    hatList.ap

    print('Lista sem o último elemento: ',hatList)

    # Step 3: write a line of code here that prints the length of the existing list.

    print('Tamando final da lista é : ',len(hatList))


def Lista_Append():
    myList = []  # creating an empty list
    for i in range(5):
        myList.append(i + 1)

    print(myList)
    print()

def Lista_Insert():
    myList = [] # creating an empty list

    for i in range(5):
        myList.insert(0, i + 1)

    print(myList)

def Lista_Total():
    myList = [10, 1, 8, 3, 5]
    total = 0

    for i in range(len(myList)):
        total += myList[i]

    print(f'Total da lista {myList} é {total}')

def Lista_Total_OK():
    myList = [10, 1, 8, 3, 5]
    total = 0

    for i in myList:
        print(i,end="-")
        total += i

    print(f'Total da lista {myList} é {total}')

# Programa Principal:

def Lista_Inversao():
    myList = [10, 1, 8, 3, 5]
    length = len(myList)
    print(myList)
    for i in range(length // 2):
        myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

    print(myList)


def Lista_beatles():
    # step 1
    beatles = []
    # step 2
    for i in range(3):
        beatles.append(input (f'Digite o {i+1}o participante da banda.'))

    print("Step 2:", beatles)

    # step 3
    Novos_Membros = int(input ("Quantos novos membros incluirá: "))
    tam = len(beatles) + 1
    for i in range(Novos_Membros):
        beatles.append(input(f'Digite o {tam +i}o participante da banda.'))
    print("Step 3:", beatles)

    # step 4
    Exclui_Membros = int(input("Quantos membros deseja excluir?: "))
    for i in range(Exclui_Membros):
        print(beatles)
        j = int (input ('Qual membro excluirá? '))
        del beatles[j-1]
    print("Step 4:", beatles)


    # step 5
    Novos_Membros = int(input("Quantos novos membros incluirá: "))
    for i in range(Novos_Membros):
        print(beatles)
        j = int(input(f'Em qual posicao incluirá o {i+1}o participante ? '))
        beatles.insert(j-1, input(f'Digite o {j}o participante da banda.'))

    print("Step 5:", beatles)


    # testing list legth
    print("Tamanho final da lista", len(beatles))

def Alimenta_Lista():
    teste = []
    teste = "1",2,3,"4"
    print (teste)
    input ("aguardo...")

def Classifica_bolha():
    myList = []
    swapped = True
    num = int(input("Quantos elementos quer classificar?: "))

    for i in range(num):
        val = float(input(f"Insira o {i+1}o elemento: "))
        myList.append(val)

    while swapped:
        swapped = False
        for i in range(len(myList) - 1):
            print (f"Analisa se o {i+2}o é maior do que o {i+1}o ", myList, end=' ')
            print(input("Enter continua..."),end='')
            if myList[i] > myList[i + 1]:
                swapped = True
                myList[i], myList[i + 1] = myList[i + 1], myList[i]
                print(f"Mudei o {i+2}o pelo {i+1}o -->", myList,end=' ')
                aguardo = input("Enter continua...")
            else: print("Sem alteração..")

    print("\nClassificado:")
    print(myList)

def Retira_Duplicado():  # 3.1.6.9 LAB: Operando com listas - básico
    myList = [] # [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    mylist2 = []
    mylist3 = []

    while True:
        elem = int(input ('Insira um número inteiro ou [0] para sair: '))
        if elem == 0: break
        myList.append(elem)

    tamanho = len(myList)

    for n in range(tamanho):
        procura = myList[n]

        if procura not in myList[n+1:]:
            mylist2.append(procura)
        else:
            mylist3.append(procura)

        #"for i in myList[n+1:]:
        # ""   if i != procura:
    print(f'Lista dos exclusivos {mylist2}')
    print(f'Lista dos excluidos {mylist3}')


    print("\nLista com os elementos únicos:")
    print(mylist2)

def Lista_avancado():
    numeros = [x for x in range (21)]
    pares = [x for x in range (20) if x % 2 == 0]
    impares = []
    print (numeros,input('Numeros. Aguarda...'))
    for x in numeros:
        if x % 2 !=0: impares.append(x)
    print (impares,input("Impares. Aguarda..."))
    print(pares, input("Pares. Aguarda..."))

def Tabuleiro():
    Peça = '1'
    board = [[Peça for i in range(8)] for j in range(8)]
    print (board)

def xadres():
    Vazio = "--"
    Peão = "Pe"
    Torre = "Tr"
    Bispo = "Bi"
    Cavalo = "Cv"
    Rei = "Re"
    Rainha = "Ra"

    tabuleiro = []

    for i in range(8):
        if i == 1 or i == 6:
            linha = [Peão for i in range(8)]
        else:
            linha = [Vazio for i in range(8)]
        tabuleiro.append(linha)
        #print(linha)

    tabuleiro[0][0] = Torre
    tabuleiro[0][7] = Torre
    tabuleiro[7][0] = Torre
    tabuleiro[7][7] = Torre

    tabuleiro[0][1] = Cavalo
    tabuleiro[0][6] = Cavalo
    tabuleiro[7][1] = Cavalo
    tabuleiro[7][6] = Cavalo

    tabuleiro[0][2] = Bispo
    tabuleiro[0][5] = Bispo
    tabuleiro[7][2] = Bispo
    tabuleiro[7][5] = Bispo

    tabuleiro[0][3] = Rei
    tabuleiro[7][4] = Rei

    tabuleiro[0][4] = Rainha
    tabuleiro[7][3] = Rainha

    for i in range(8): print(tabuleiro[i])

    print(tabuleiro[7][7])

while True:
   # Lista_Chapeu()
   # Lista_Append()
   # Lista_Insert()
   # Lista_Total()
   # Lista_Total_OK()
   # Lista_Inversao()
   # Lista_beatles()
   #Alimenta_Lista()
   #Classifica_bolha()
   # Retira_Duplicado()
   # Lista_avancado()
   # Tabuleiro()
    xadres()
    sair = input('Deseja repetir? ')
    if sair[0].upper() == "S" : continue
    print ('\n Fim do programa\n')
    break

