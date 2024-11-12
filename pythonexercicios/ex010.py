# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Qual o valor do produto? "))
d = (5 / 100) * p
de = p - d
print("Na liquidação, o preço desse prodito, que é {}R$ com 5% de desconto fica {}R$".format(p, de))
