#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
n1 = float(input("Digite sua nota "))
n2 = float(input("Digite sua outra nota "))
m = (n1 + n2)/2
print("Voce tirou a nota {}, e também a nota {}, sua média é {} ".format(n1, n2, m))