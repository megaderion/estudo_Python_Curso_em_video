#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas
#Quantas letras ao todo (Sem considerar os espaços)
#Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúscula é {}" .format(nome.upper()))
print("Seu nome em minúscula é {}" .format(nome.lower()))
print("Seu nome tem ao todo {} letras" .format(len(nome) - nome.count("  ")))
#print("O seu primeiro nome tem {} letras" .format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome e {} e ele tem {} letras" .format(separa[0], len(separa[0])))