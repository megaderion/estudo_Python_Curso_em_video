#EScreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input("Quantos metros você tem? "))
c = m * 100
mi = m * 1000
print("Já que você tem {} metros, então terá {:.0f} centimetros e {:.0f} milimetros".format(m, c, mi))