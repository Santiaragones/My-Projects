import random
import re

lista_palabras=['Hola', 'Chau', 'Ojo', 'Pizza', 'Enojado', 'Fuego', 'Calabaza', 'Bebe', 'Flor', 'Arco', 'Barba',
	'Platillo', 'volador', 'Reciclar', 'Biblia', 'Jirafa', 'Castillo', 'Arena', 'Bikini', 'Gafas', 'Nieve', 'Libro',
	'Tacon', 'Escalera', 'Cucurucho', 'Helado', 'Estrella', 'Mar', 'Abejorro', 'Iglu', 'Fresa', 'Mariposa', 'Escarabajo',
	'Sol', 'Camara', 'Lampara', 'Neumatico', 'Gato', 'Leon', 'Tostada', 'Iglesia', 'Buzon', 'Cepillo', 'Dientes', 'Lapiz',
	'Color', 'Noche', 'Pasta', 'Dental', 'Delfin', 'Nariz', 'Camion', 'Huevo', 'Juegos', 'Olimpico', 'Voleibol', 'Torre', 'Mani']

print('Quieres empezar a jugar?')
print('Escribe SI para empezar')
respuesta=input()
respuesta=respuesta.upper()

#while respuesta!='SI':
	#print('Escribe SI para empezar')
	

if respuesta == 'SI':
	palabra_oculta=random.choice(lista_palabras)
	palabra_oculta=palabra_oculta.upper()


letras_faltantes=len(palabra_oculta)
vidas=len(palabra_oculta)+3

while letras_faltantes != 0 and vidas>0:
	letra=input('Introduce una letra (mayúscula):')

	if re.search(letra, palabra_oculta):
		print('\nLetra correcta!')
		letras_faltantes=letras_faltantes-1

		indice=palabra_oculta.find(letra)
		for i in palabra_oculta:
			print(palabra_oculta[indice])
		
	else:
		print('\nLetra incorrecta')
		vidas=vidas-1
		print('Vidas restantes: {}'.format(vidas))



if letras_faltantes==0:
	print('Ganaste!')

else:
	print('Perdiste, te quedaste sin vidas.')







