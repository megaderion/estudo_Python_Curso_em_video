#Faça um programa que leia algo pelo teclado e mostre nela o seu tipo primitivo  e todas as informações possiveis sobre ele.

n = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(n))
print("so tem espaços? ", n.isspace())
print("é um numero?", n.isnumeric())
print("é um alfabeto? ", n.isalpha())
print("é um alfanumerico? ", n.isalnum())
print("está em maiuscula? ", n.isupper())
print("Está em minuscula? ", n.islower())
print("Está capitalizada?", n.istitle())