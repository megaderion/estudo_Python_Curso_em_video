#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#co = float(input("comprimento do cateto oposto: "))
#ca = float(input("comprimento do cateto adjancente: "))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print("a hipotenusa vai medir {:.2f}" .format(hi))

#import math
#co = float(input("comprimento do cateto oposto: "))
#ca = float(input("comprimento do cateto adjancente: "))
#hi = math.hypot(co, ca)
#print("a hipotenusa vai medir {:.2f}" .format(hi))

from math import hypot
co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjancente: "))
hi = hypot(co, ca)
print("a hipotenusa vai medir {:.2f}" .format(hi))