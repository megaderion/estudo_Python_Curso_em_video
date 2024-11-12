# Tenho um rolo de papel de parede de 5.40m e quero saber quantos rolos para uma parede inteira

pa = float(input("Qual a altura da parede? "))
pl = float(input("qual a largura da parede? "))
m2 = pa*pl
r = 5.4 * m2
print("Você precisará de {:.2f}m de rolo para {:.2f}m² ".format(r, m2))