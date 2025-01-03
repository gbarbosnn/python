# Solicitar ao usuário o raio de um circulo e calcular
# a área (A = πr^2) e o volume de uma esfera com esse raio (V= 4/3πr^3)

import math

raio = input('informe um raio: ')

area = math.pi * float(raio) ** 2
volume = (4/3) * math.pi * float(raio) ** 3

print(f"a área é: {area}²")
print(f"o volume é: {volume}³")
