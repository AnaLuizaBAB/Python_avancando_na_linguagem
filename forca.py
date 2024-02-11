def jogar():

    print("\n\n")
    print ("Bem vindo ao jogo da forca.")
    print("\n")

    
    palavra_secreta = 'banana'
    enforcado = False
    acertou = False

    while((enforcado == False) and (acertou == False)):
        index = 0                                                           # se o index for declarado antes do while retornará a posição errada.
        chute = (input("Digite uma letra:")).lower().strip()
        for letra in palavra_secreta:
            if (letra == chute):
                print( f"A letra {chute} foi encontrada na posição {index}")
            index = index + 1
        print("Tente novamente.")

    print("\nFim de Jogo.")

if(__name__ == "__main__"):
    jogar()