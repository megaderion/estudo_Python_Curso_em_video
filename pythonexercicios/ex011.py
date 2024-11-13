# Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input("Qual o seu salário? "))
a = (s * 15 / 100) + s
print("Seu salário de {:.2f}R$ com 15% de aumento vai ficar {:.2f}R$".format(s, a))