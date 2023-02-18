import forca
import adivinhacao

def escolher_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) Forca (2) Adivinahção")

    jogo = int(input("Qual o jogo deseja escolher?"))

    if (jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação!")
        adivinhacao.jogar()
        
if(__name__ == "__main__"):
    escolher_jogo()
