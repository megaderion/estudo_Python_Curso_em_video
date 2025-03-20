#nome = str(input("Qual o seu nome? "))
#if nome == "Matheus":
 #   print("Que nome dahora tio ")
#else:
 #   print("Seu nome não e tão dahora assim ")
#print("Bom dia, {}".format(nome))

n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
m = (n1 + n2)/ 2
print("Sua nota foi {:.1f}".format(m))
#if m >= 6:
 #   print("Passou em tiozao, parabéns ")
#else:
 #   print("Deu ruim, muito burro kkkkk")
print("Parabéns" if m >=6 else "Estude mais")