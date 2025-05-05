#numero = float(input("Digite um número: "))

#if numero > 0:
 #   print("O número é positivo ")
#elif numero < 0:
   # print("O número é negativo ")
#else:
  #  print("O número é zero") 

#=========== calculadora =============

#numero1 = float(input("Digite o primeiro número "))
#numero2 = float(input("Digite o segundo número "))
#operacao = input("Digite (+, -, *, /): ")

#if operacao == '+':
 #   resultado = numero1 + numero2
  #  print("resultado ", resultado)
#elif operacao == '-':
 #   resultado = numero1 - numero2
  #  print("resultado ", resultado)
#elif operacao == '*':
 #   resultado = numero1 * numero2
  #  print("resultado ", resultado)
#elif operacao == '/':
 #   if numero2 != 0:
  #      resultado = numero1 / numero2
   #     print("resultado ", resultado)
   # else:
    #    print("Erro: divisão invalida")
#else:
 #   print("operação invalida.")

#-============== calculando idade =============

#idade = int(input("Digite sua idade: "))

#if idade >=0 and idade <= 12:
 #   print("Vocé é uma criança")
#elif idade >= 13 and idade <= 17:
 #   print("Você é um adolescente")
#elif idade >= 18 and idade <= 59:
#    print("Você é um adulto ")
#elif idade >= 60:
#    print("Você é um idoso")
#else:
#    print("Idade invalida")

#======= ano bissexto =========

#ano = int(input("Digite um ano: "))
#if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
 #   print(ano, "é um ano bissexto")
#else:
 #   print(ano, "não é um ano bissexto")

#================ caixa eletronico =============

valor_saque = int(input("Digite um valor de saque: R$"))
if valor_saque <= 0:
    print("Valor invalido")
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100

    cedulas_50 = valor_saque // 50
    valor_saque %= 50

    cedulas_20 = valor_saque // 20
    valor_saque %= 20

    cedulas_10 = valor_saque // 10
    valor_saque %= 10

    cedulas_5 = valor_saque // 5
    valor_saque %= 5

    cedulas_2 = valor_saque // 2
    valor_saque %= 2

    if valor_saque != 0:
        print("Não é possivel sacar o valor especifico com as cédulas disponíveis.")
    else:
        print("Cédulas entregues: ")
        if cedulas_100 > 0:
            print(f"{cedulas_100} x R$100")
        if cedulas_50 > 0:
            print(f"{cedulas_50} x R$50")
        if cedulas_20 > 0:
            print(f"{cedulas_20} x R$20")
        if cedulas_10 > 0:
            print(f"{cedulas_10} x R$10")
        if cedulas_5 > 0:
            print(f"{cedulas_5} x R$5")
        if cedulas_2 > 0:
            print(f"{cedulas_2} x R$2")