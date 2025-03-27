#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-="*15)
print("Analisando triângulos")
print("-="*15)
r1 = float(input("primeir segmento "))
r2 = float(input("segundo segmento "))
r3 = float(input("terceiro segmento "))
if r1 < r3 + r2 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses segmentos PODEM FORMAR um triângulo")
else:
    print("Esses segmentos NÃO PODEM formar um triângulo")