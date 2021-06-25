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
from DISClib.Algorithms.Sorting import insertionsort as so
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
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

def getLikedVideos(catalog, category_name,country, numerovideos,sorting):
    for i in range (1, lt.size(catalog['categories']+1)):
        lista_categorias = catalog['categories']
        categoria = lt.getElement(lista_categorias, j)
        if categoria['name']== category_name:
            id = categoria['category_id']
    lista_inicial = catalog['videos']
    lista_sortear= lt.newList('ARRAY_LIST')
    for j in range(1,lt.size(catalog['videos']+1):
        video = lt.getElement(lista_inicial, j)
        if video["category_id"] == id:   
            if video["country"] == country:
                lt.addLast(lista_sortear, video)
    sortVideos(lista_sortear,sorting)
    sublista = lt.subList(lista_sortear,1 , numerovideos)
    return sublista

def subList(catalog, numerovideos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        catalog: La lista a examinar
        numerovideos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lt.subList(lst, numerovideos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')    

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByLikes(video1, video2):
""" Devuelve verdadero (True) si los likes de video1 
son menores que los del video2 Args: video1: informacion del 
primer video que incluye su valor 'likes'"""
    return (video1['likes']) < (video2['likes']))
# Funciones de ordenamiento

def sortVideos(lista,sorting):
    if sorting == 1:
        start_time = time.process_time() 
        sorted_list = sa.sort(lista,cmpVideosByLikes) 
        stop_time = time.process_time() 
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    elif sorting == 2:
        sub_list = lt.subList(catalog['videos'], 1, size) 
        sub_list = sub_list.copy() 
        start_time = time.process_time() 
        sorted_list = se.sort(sub_list,cmpVideosByLikes) 
        stop_time = time.process_time() 
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    else:
        sub_list = lt.subList(catalog['videos'], 1, size) 
        sub_list = sub_list.copy() 
        start_time = time.process_time() 
        sorted_list = so.sort(sub_list,cmpVideosByLikes) 
        stop_time = time.process_time() 
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list