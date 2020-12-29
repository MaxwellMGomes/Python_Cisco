

'''
se a renda do cidadão não for superior a 85.528 táleres, o imposto será igual a 18% da renda 
menos 556 táleres e 2 centavos (este era o chamado alívio fiscal )

se a renda fosse superior a esse valor, o imposto era igual a 14.839 táleres e 2 centavos, 
mais 32% do excedente sobre 85.528 táleres.

'''

while True:
    Renda = float(input("Entre com sua renda anual: "))
    if Renda == 0 : break
    if Renda <= 85528 : taxa = Renda * 18/100 - 556.02
    elif Renda > 85528: taxa = 14839.02 + (Renda - 85528) * 32/100
    else : Renda = 0

    if taxa <= 0 : taxa = 0
    else : taxa = round(taxa, 0)
    print(f"Para uma renda de {Renda}, o imposto devido é de {taxa} thalers")

