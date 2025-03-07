#Crie um arquivo chamado meu_modulo.py e dentro dele defina uma função chamada dobro(n), que retorna o dobro de um número. Depois, crie outro arquivo Python que importe meu_modulo e utilize a função dobro() para exibir o dobro de um número informado pelo usuário.

import meu_modulo

numero = int(input("digite um número: "))
resultado = meu_modulo.dobro(numero)

print("o dobro de {} é {}" . format(numero, resultado))