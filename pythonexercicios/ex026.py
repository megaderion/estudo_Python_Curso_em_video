# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O Programa deverá escrever na tela se o usuario venceu ou perdeu

from random import randint
from time import sleep
comp = randint(0,5) #Faz o computador pensar
print("'-=-'" *10)
print("Vou pensar em um número, tente adivinhar...")
print("'-=-'" *10)
player = int(input("Em que número pensei ... ")) #jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)
if player == comp:
    print("Acertou miseravi")
else:
    print("Errou krl, em pensei no {} e não no {}".format(comp, player))
