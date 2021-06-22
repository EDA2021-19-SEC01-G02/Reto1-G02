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
    return (float(book1['average_rating']) < float(book2['average_rating']))
# Funciones de ordenamiento
def insertionsort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpfunction(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst

def selectionsort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst, pos2),
               (lt.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

def shellsort(lst, cmpfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpfunction(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst

def sortVideos(catalog):
    if sorting == 1:
        sub_list = lt.subList(catalog['videos'], 1, size) 
        sub_list = sub_list.copy() 
        start_time = time.process_time() 
        sorted_list = sa.insertionsort(sub_list,cmpVideosByLikes) 
        stop_time = time.process_time() 
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    elif sorting == 2:
        sub_list = lt.subList(catalog['videos'], 1, size) 
        sub_list = sub_list.copy() 
        start_time = time.process_time() 
        sorted_list = sa.selectionsort(sub_list,cmpVideosByLikes) 
        stop_time = time.process_time() 
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    else:
                sub_list = lt.subList(catalog['videos'], 1, size) 
        sub_list = sub_list.copy() 
        start_time = time.process_time() 
        sorted_list = sa.shellsort(sub_list,cmpVideosByLikes) 
        stop_time = time.process_time() 
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    