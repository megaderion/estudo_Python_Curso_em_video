# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input("Qual a distancia? "))
if viagem <= 200:
    passagem = viagem * 0.5
    print("Sua passagem deu R${:.2f}" .format(passagem))
else:
    passagem = viagem * 0.45
    print("Sua passagem deu R${:.2f}" .format(passagem))