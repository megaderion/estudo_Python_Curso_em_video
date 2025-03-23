# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Qual a velocidade atual do veículo? "))
if vel > 80:
    print("Multado, você excedeu o limite de 80km! ")
    multa = (vel-80)*7
    print("Você deve pagar a multade R${:.2f} ".format(multa))
print("Tenha um bom dia, Dirija com segurança!")