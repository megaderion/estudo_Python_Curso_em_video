# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Qual o valor do produto? "))
d = p - (p * 5 / 100)
print("Na liquidação, o preço desse prodito, que é {:.2f}R$ com 5% de desconto fica {:.2f}R$".format(p, d))
