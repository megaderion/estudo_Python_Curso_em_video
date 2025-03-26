# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Digite um número "))
b = int(input("Digite um número "))
c = int(input("Digite um número "))
# verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("o menor valor foi {} e o maior digitado foi {}".format(menor, maior))