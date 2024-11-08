# Crie um programa que leia, quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. considere = 1US$1,00 = R$ 5,69

D = float(input("Digite quanto você tem em R$ "))
U = D / 5.69
print("Com {}R$ você consegue comprar {:.2f}U$ Dolares".format(D, U))