# Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input("Qual o seu salário? "))
a = (15 / 100) * s
au = a + s
print("Seu salário de {}R$ com 15% de aumento vai ficar {}R$".format(s, au))