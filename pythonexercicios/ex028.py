# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número "))
resul = num % 2
if resul == 0:
    print("o número {} é PAR ".format(num))
else:
    print("O número {} é IMPAR".format(num))