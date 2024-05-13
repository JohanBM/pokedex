import requests
import matplotlib.pyplot as plt
import shutil
from PIL import Image
from urllib.request import urlopen

pokemon = input("Nombre del pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
respuesta = requests.get(url)

if respuesta.status_code != 200:
    print("No se encontro el pokemon")
    exit()

datos = respuesta.json()
#######################################################
#Imagen del pokemon
try:
    urlImagen = datos["sprites"]['front_default']
    imagen = Image.open(urlopen(urlImagen))

    f_archivo = open(pokemon + '.json', "w")
    f_archivo.write(urlImagen)
    f_archivo.close()

except:
    print("No se encontro el pokemon")
    exit()

plt.title(datos['name'])
imgplot = plt.imshow(imagen)

plt.show()
######################################################
#caracteristicas del pokemon
datos = respuesta.json()
nombre = datos["name"]
tipos = datos["types"]
habilidades = datos["abilities"]
alturas = datos["height"]
pesos = datos["weight"]

with open(pokemon +'.json', "a") as f_archivo:
    f_archivo.write('\n' + nombre)

print('Nombre: ', nombre)
print('Tipo: ')

for i in range(len(datos['types'])):
    tipo = tipos[i]['type']['name']
    print(tipo)

    with open(pokemon + '.json', "a") as f_archivo:
        f_archivo.write('\n' + tipo)

print('Habilidades:')
for i in range(len(datos["abilities"])):
    habilidad = habilidades[i]["ability"]['name']
    print(habilidad)

    with open(pokemon + '.json', "a") as f_archivo:
        f_archivo.write('\n' + habilidad)

altura = alturas / 10
print(f'Altura: ' + repr(altura) + 'm')
peso = pesos / 10
print(f'Peso: ' + repr(peso) + 'kg')
with open(pokemon + '.json', "a") as f_archivo:
    f_archivo.write('\nSu peso es ' + repr(peso) + 'kg')
    f_archivo.write('\nSu altura es ' + repr(altura) + 'm')

print('\n')
#####################################################
#Movimientos del pokemon
with open(pokemon + '.json', "a") as f_archivo:
    f_archivo.write('\n Lista de movimientos del pokemon')
print ('movimientos del pokemon ' + nombre + ':')
movimientos = datos["moves"]
for i in range(len(movimientos)):
    movimiento = movimientos[i]['move']['name']
    print(movimiento)

    with open(pokemon + '.json', "a") as f_archivo:
        f_archivo.write('\n' + movimiento)

############################################################
#Mandar archivo creado a la carpeta pokedex
shutil.move(pokemon + '.json', 'pokedex')
