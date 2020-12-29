"""
 A pirâmide é empilhada de acordo com um princípio simples:
  cada camada inferior contém um bloco a mais do que a camada acima.

Sua tarefa é escrever um programa que leia o número de blocos que os construtores possuem
 e produza a altura da pirâmide que pode ser construída usando esses blocos.

Nota: a altura é medida pelo número de camadas totalmente concluídas - se os construtores não tiverem
um número suficiente de blocos e não puderem concluir a próxima camada, eles terminam seu trabalho imediatamente."""

blocos = 0
while blocos != -1:
    blocos = int (input("insira o número de blocos: "))
    soma_bloco = 0
    altura = 0
    while True:
        if soma_bloco < blocos:
            soma_bloco += altura
            if soma_bloco > blocos:
                 print ("\033[;31mNão há blocos suficiente para montar a piramide!\033[m")
                 altura -=1
                 break
            if soma_bloco == blocos: continue
            altura += 1
        else: break
    print(f"\033[;34mA altura da piramide é : {altura}\033[m")
