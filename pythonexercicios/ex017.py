#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#import random
#n1 = str(input("Primeiro aluno "))
#n2 = str(input("Segundo aluno "))
#n3 = str(input("Terceiro aluno "))
#n4 = str(input("Quarto aluno "))
#lista = [n1, n2, n3, n4]
#random.shuffle
#print("A sequencia de apresentação, será ")
#print(lista)

from random import shuffle
n1 = str(input("Primeiro Aluno "))
n2 = str(input("Segundo Aluno "))
n3 = str(input("Terceiro Aluno "))
n4 = str(input("Quarto Aluno "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A sequencia de apresentação sera ")
print(lista)