# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tina pinta uma área de 2m²

a = float(input("Qual a altura da parede? "))
l = float(input("Qual a largura da parede? "))
m2 = a * l
t = m2 / 2
print("Precisaremos de {:.2f} litros de tinta para pintar {:.2f}m²".format(t, m2))