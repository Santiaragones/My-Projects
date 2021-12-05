import random

lista_colores=[]

color1=input("Introduce un color: ")
lista_colores.append(color1)

color2=input("Introduce un color: ")
lista_colores.append(color2)

color3=input("Introduce un color: ")
lista_colores.append(color3)

m=random.choice(lista_colores)
print(m)

input()