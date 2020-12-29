'''Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante
(ainda não foi comprovada) que pode ser descrita da seguinte forma:

pegue qualquer número inteiro não negativo e diferente de zero e nomeie-o c0;
se for par, avalie um novo c0como c0 ÷ 2;
caso contrário, se for estranho, avalie um novo c0como 3 × c0 + 1;
se c0 ≠ 1, pule para o ponto 2.
A hipótese diz que independentemente do valor inicial de c0, ele sempre irá para 1.'''

c0 = int(input("Digite um número inteiro e positivo: "))
etapa = 0
while c0 != 1:
    if c0 % 2 == 0: c0 = c0 / 2
    else: c0 = 3 * c0 + 1
    print (int(c0),end='/')
    etapa += 1

print("\npassos = ",etapa)