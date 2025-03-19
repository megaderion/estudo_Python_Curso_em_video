#Faça um programa que leia o nome completo de uma pessoa, mostrando em segua o primeiro e o ultimo nome separadamente

nome = str(input("Qual o seu nome? ")).strip()
n = nome.split()
#print("Seu nome completo é {}".format(nome))
print("Seu primeiro nome é {}".format(n[0]))
print("Seu ultimo nome {}".format(n[len(n)-1]))