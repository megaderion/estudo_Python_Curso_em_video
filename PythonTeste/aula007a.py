#para quebrar a linha "\n" 
#para não quebrar a linha, no final do print digitar "end= ' '" 

n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 

print("a soma e {}, \n o produto é {}, \n e a divisão é {:.3f} ".format(s, m, d), end=' ')
print("Divisão inteira {}, e potencia {}".format(di, e)) 