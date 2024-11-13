# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: Digirte um número: 6.127, o número tem a parte inteira 6
import math
num = float(input("Digite um numero "))

print("O número tem a parte inteira {}".format( math.trunc(num)))