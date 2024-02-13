def jogar():

    print("\n\n")
    print ("Bem vindo ao jogo da forca.")
    print("\n")

    
    palavra_secreta = 'banana'.lower()
    enforcado = False
    acertou = False
    numero_da_tentativa = 1                                                 # se eu colocar esse index dentro do wile da errado!! PQ??

    # decidir o nível de dificuldade

    print ("Informe o nível de dificuldade desejada")
    print("1 (Fácil)     2 (Médio)     3 (Difícil)")
    nivel_dificuldade = int(input("\nQual é o nível de dificuldade desejado?"))

    if (nivel_dificuldade == 1):
        tentativas = 15
    elif (nivel_dificuldade == 2):
        tentativas = 9
    else:
        tentativas = 6

    # Colocando um '_' para cada letra da palavra secreta
        
    lista = []

    for letra in palavra_secreta:                                           # para colocar a quantidade de "_" de acordo com o tamanho da palavra secreta!
        lista.append('_')
    
    print ('\n')
    print (lista)

    # início do loop:

    while((enforcado == False) and (acertou == False)):
        
        index = 0                                                               # se o index for declarado antes do while retornará a posição errada.
        chute = (input("\nDigite uma letra:")).lower().strip()
        for letra in palavra_secreta:
            if (letra == chute):
                lista.pop(index)                                            # Retira o '_' na posição indicada e na linha abaixo é substituida pela letra correspondente.
                lista.insert(index, chute)
            index = index + 1

        if(lista.count("_")) == 0:
            print(lista)
            print("\nParabéns! Você acertou a palavra.")
            break
        elif(numero_da_tentativa == tentativas) and ((lista.count("_")) != 0):
            print(lista)
            print("Você foi enforcado!!!")
            break
        else:
            print(f"Tentativa {numero_da_tentativa}")
            print(lista)
        numero_da_tentativa = numero_da_tentativa + 1

            
    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()