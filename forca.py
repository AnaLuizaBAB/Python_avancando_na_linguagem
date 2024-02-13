def jogar():

    print("\n\n")
    print ("Bem vindo ao jogo da forca.")
    print("\n")

    
    palavra_secreta = 'banana'
    enforcado = False
    acertou = False
    numero_da_tentativa = 2                                              # se eu colocar esse index dentro do wile da errado!! PQ??

    lista = []

    for letra in palavra_secreta:                                           # para colocar a quantidade de "_" de acordo com o tamanho da palavra secreta!
        lista.append('_')
    
    print (lista)
    print('\n')

    while((enforcado == False) and (acertou == False)):
        
        index = 0                                                               # se o index for declarado antes do while retornará a posição errada.
        chute = (input("Digite uma letra:")).lower().strip()
        for letra in palavra_secreta:
            if (letra == chute):
                lista.pop(index)                                            # Retira o '_' na posição indicada e na linha abaixo é substituida pela letra correspondente.
                lista.insert(index, chute)
            index = index + 1

        if(lista.count("_")) == 0:
            print(f"\nTentativa {numero_da_tentativa}")
            print(lista)
            print("\nParabéns! Você acertou a palavra.")
            break
        else:
            print(lista)
            print(f"\nTentativa {numero_da_tentativa}")
        numero_da_tentativa = numero_da_tentativa + 1
    
    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()