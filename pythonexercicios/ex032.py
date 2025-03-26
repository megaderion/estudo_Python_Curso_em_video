# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salário para o ajueste R$"))
if salario <= 1250:
    novosal = salario + (salario * 15 / 100)
else:
    novosal = salario + (salario * 10 / 100)
print("Seu reajuste foi calculado, o salario que era R${} passa a ser R${}".format(salario, novosal))