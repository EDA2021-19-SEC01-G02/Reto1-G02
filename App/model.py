"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.Algorithms.Sorting import quicksort as se
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as sa

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(format):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una para las categorías. Retorna el catalogo inicializado.
    """
    if format == 1:
        format = 'ARRAY_LIST'
    elif format == 2:
        format = 'LINKED_LIST'

    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList(format)
    catalog['categories'] = lt.newList(format)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, id, name):
    """
    Adiciona un tag a la lista de tags
    """
    c = newCategory(id, name)
    lt.addLast(catalog['categories'], c)

# Funciones para creacion de datos

def newCategory(id, name):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    category = {'name': '', 'category_id': ''}
    category['name'] = name.strip()
    category['category_id'] = id
    return category

def getLikedVideos(catalog, category_name,country, numerovideos,sorting,muestra):
    
    #Codigo solo para el lab 4
    lista_muestra = lt.subList(catalog['videos'],1,muestra)
    t, lista_muestra = sortVideos(lista_muestra, sorting)
    print(t)
    return None

    """
    id = -1000
    sublista = None

    for i in range(1, lt.size(catalog['categories'])+1):
        categoria = lt.getElement(catalog['categories'], i)
        if categoria['name'].lower() == category_name.lower():
            id = categoria['category_id']
    if id == -1000:
        print('No existe esa categoría')
    else:    
        lista_inicial = catalog['videos']
        lista_sortear= lt.newList('ARRAY_LIST')

        for j in range(1,lt.size(catalog['videos'])+1):
            video = lt.getElement(lista_inicial, j)
            if video["category_id"] == id and video["country"].lower().strip() == country.lower():   
                lt.addLast(lista_sortear, video)

        t, lista_sortear = sortVideos(lista_sortear, sorting)
        if numerovideos <= lt.size(lista_sortear):
            sublista = lt.subList(lista_sortear, 1, numerovideos)
        else:
            print('No hay suficientes videos en la lista')
            
    
    return sublista    
    """

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByLikes(video1, video2):
    """ Devuelve verdadero (True) si los likes de video1 
    son menores que los del video2 Args: video1: informacion del 
    primer video que incluye su valor 'likes'"""
    return (int(video1['likes'])) > int((video2['likes']))
# Funciones de ordenamiento

def sortVideos(lista,sorting):
    if sorting == 'MERGE_SORT':
        start_time = time.process_time() 
        sorted_list = sa.sort(lista,cmpVideosByLikes) 
        stop_time = time.process_time() 
        t = (stop_time - start_time)*1000
    else:
        start_time = time.process_time() 
        sorted_list = se.sort(lista,cmpVideosByLikes) 
        stop_time = time.process_time() 
        t = (stop_time - start_time)*1000
    return t, sorted_list