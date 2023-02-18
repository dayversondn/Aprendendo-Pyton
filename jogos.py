import forca
import adivinhacao

print("********************************")
print("*******Escolha o seu jogo*******")
print("********************************")

print("(1) Forca (2) Adivinahção")

jogo = int(input("Qual o jogo deseja escolher?"))

if (jogo == 1):
    print("Jogando forca!")
elif(jogo == 2):
    print("Jogando adivinhação!")

