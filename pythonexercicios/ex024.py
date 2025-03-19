#Faça um programa que leia uma frase no teclado e mostre quantas vezes aparece a letra "A", em que posição aparece a primeira vez e em que posição aparece a ultima vez

frase = str(input("Digite uma Frase: ")).upper().strip()
print("A letra A aparece {} vezes ".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}" .format(frase.find("A")+1))
print("A ultima vez que a letra A parece e na posição {}" .format(frase.rfind("A")+1))