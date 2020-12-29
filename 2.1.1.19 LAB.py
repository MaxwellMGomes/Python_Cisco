print("Programming","Essentials","in ",end='',sep='*')
print("Python")



def seta_padrao():
    print("    *")
    print("   * *")
    print("  *   *")
    print(" *     *")
    print("***   ***")
    print("  *   *")
    print("  *   *")
    print("  *****")
    print()


def multi_seta():
    qset = int(input ('Quantas Setas?'))
    print("    *     "*qset)
    print("   * *    "*qset)
    print("  *   *   "*qset)
    print(" *     *  "*qset)
    print("***   *** "*qset)
    print("  *   *   "*qset)
    print("  *   *   "*qset)
    print("  *****   "*qset)


def seta_linha():
    print("     *     \n","   * *    \n","  *   *   \n"," *     *  \n","***   *** \n","  *   *   \n","  *   *   \n","  *****   ")
    print()


def aumenta_seta(lat_info=4):
    q_tronco = lat_info //2
    lateral = lat_info // 2 * 2

    interno = lateral - 3
    # interno = 1
    tronco = 0

    lat_plus = lateral + q_tronco - 2
    int_plus = 1
    print(" " * lat_plus + "*" + " " * lat_plus)
    lat_plus -= 1

    while lat_plus >= lateral:
        print(" " * lat_plus + "*" + " " * int_plus + "*" + " " * lat_plus)
        lat_plus -= 1
        int_plus += 2

    lateral -= 1  # original
    lat_plus += 2

    while lateral > 0:
        print(" " * lateral + "*" + " " * interno + "*" + " " * lateral)    # alterei de lateral para lat_plus
        lateral -= 1
        interno += 2
        tronco += 1


    # Montando o Tronco
    tronco_interno = tronco + 2
    tronco_externo = tronco - 1
    print("*" * tronco + " " * tronco + "*" * tronco)
    for i in range(q_tronco):
        print(" " * tronco_externo + "*" + " " * tronco + "*" + " " * tronco_externo)

    print(" " * tronco_externo + "*" * tronco_interno + " " * tronco_externo)



#seta_padrao()
#multi_seta()
#seta_linha()
aumenta_seta(int(input("Qual tamanho da arvore ")))

"""print(" "*lateral+"*"+" "*lateral)
lateral -= 1
print(" "*lateral+"*"+" "*interno+"*"+" "*lateral)
lateral -= 1
interno +=2
tronco +=1
print(" "*lateral+"*"+" "*interno+"*"+" "*lateral)
lateral -= 1
interno +=2
tronco +=1
print(" "*lateral+"*"+" "*interno+"*"+" "*lateral)
tronco +=1
"""