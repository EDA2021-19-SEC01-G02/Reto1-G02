"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los videos con mas likes")
    print("3- Consultar  el video trending el mayor numero de dias")
    print("4- Consultar video trending con percepcion sumamente positiva")
    print("5- Consultar videos con mas comentarios por tag")
    print("0- Salir")


def initCatalog(format):
    return controller.initCatalog(format)


def loadData(catalog):
    controller.loadData(catalog)

def printLikedVideos(lista):
    for i in range(1,lt.size(lista)+1):
        video = lt.getElement(lista,i)
        print('Nombre: {} \t Likes:{}'.format(video['title'],video['likes']))

def printComentariosVideos(lista_):
    for k in range(1,lt.size(lista_)+1):
        video_ = lt.getElement(lista_,k)
        print('Nombre: {} \t Channel Title:{}'.format(video_['title'],video_['channel_title']))
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print('Seleccione la forma en que quiere cargar los datos')
        print("1- Array list")
        print("2- Lista simplemente encadenada")
        format = int(input('Seleccione una opción para continuar\n'))

        print("Cargando información de los archivos ....")
        catalog = initCatalog(format)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        
        print('Titulo primer video: ' + str(lt.firstElement(catalog['videos'])['title'])
        +', Titulo del canal: ' + str(lt.firstElement(catalog['videos'])['channel_title'])
        +', Dia que estuvo trending: ' + str(lt.firstElement(catalog['videos'])['trending_date'])
        +', Pais: ' + str(lt.firstElement(catalog['videos'])['country'])
        +', Visitas: ' + str(lt.firstElement(catalog['videos'])['views'])
        +', Likes: ' + str(lt.firstElement(catalog['videos'])['likes'])
        +', Dislikes: ' + str(lt.firstElement(catalog['videos'])['dislikes']))
        
        print('Categorias cargadas:')
        print(catalog['categories'])

    elif int(inputs[0]) == 2:
        """ 
        category_name = input("Ingrese la categoria a buscar: ")
        country = input("Ingrese el pais a buscar: ")
        numerovideos = int(input("Ingrese el numero de videos que quiere listar: "))
        solo laboratorio
        """
        print('Seleccione el tipo de algoritmo recursivo')
        print("1- Mergesort")
        print("2- Quicksort")
        sorting = input("Ingrese el tipo de algoritmo iterativo: ")

        if sorting == 1:
            sorting = 'MERGE_SORT'
        else:
            sorting = 'QUICK_SORT'
     


        #Codigo solo para el lab 4
        muestra = int(input('Ingrese el tamaño de la muestra: '))
        category_name = None
        country = None
        numerovideos = None


        mas_likes = controller.getLikedVideos(catalog, category_name, country, numerovideos, sorting, muestra)

        if mas_likes != None:
            printLikedVideos(mas_likes)

    elif int(inputs[0]) == 3:
        country = input("Ingrese el pais a buscar: ")
        trending_positiva = controller.getAltamentePositiva(catalog, country)
        printAuthorData(trending_positiva)

    elif int(inputs[0]) == 4:
        category_name = input("Ingrese la categoria a buscar: ")
        trending_positiva = controller.getSumamentePositiva(catalog, category_name)
        printSumamentePositiva(trending_positiva)

    elif int(inputs[0]) == 5:
        country = input("Ingrese el pais a buscar: ")
        numerovideos = input("Ingrese el numero de videos que quiere listar: ")
        tag = input("Ingrese la etiqueta del video: ")
        mas_comentarios = controller

        printComentariosVideos(mas_comentarios)

    else:
        sys.exit(0)
sys.exit(0)
