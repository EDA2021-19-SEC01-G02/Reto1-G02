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
from DISClib.Algorithms.Sorting import mergesort as sa

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una para las categorías. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categories'] = lt.newList('ARRAY_LIST')

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

def getLikedVideos(catalog, category_name,country, numerovideos):
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

        lista_sortear = sortVideosLikes(lista_sortear)
        if numerovideos <= lt.size(lista_sortear):
            sublista = lt.subList(lista_sortear, 1, numerovideos)
        else:
            print('No hay suficientes videos en la lista')
    return sublista   

def getSumamentePositiva(catalog, category_name):
    id = -1000
    lista_sortear= lt.newList('ARRAY_LIST')
    for i in range(1, lt.size(catalog['categories'])+1):
        categoria = lt.getElement(catalog['categories'], i)
        if categoria['name'].lower() == category_name.lower():
            id = categoria['category_id']
    if id == -1000:
        print('No existe esa categoría')
    else:
        lista_inicial = catalog['videos']
        for j in range(1,lt.size(catalog['videos'])+1):
            video = lt.getElement(lista_inicial,j)
            if int(video["dislikes"])>0:
                ratio = int(video["likes"])/int(video["dislikes"])
                if video["category_id"] == id and ratio> 20:
                    lt.addLast(lista_sortear, video)
            
    return Conteo_trending(catalog, lista_sortear)

def Conteo_trending(catalog,lista):
    conteo = {}
    lista_inicial = catalog['videos']
    for i in range (1,lt.size(lista)+1):
        id = lt.getElement(lista,i)
        id = id["video_id"]
        for j in range(1,lt.size(catalog['videos'])+1):
            video = lt.getElement(lista_inicial, j) 
            if video["video_id"] == id:
                if id in conteo.keys():
                    conteo[id]=+1
                else:
                    conteo[id]=1

    conteo=pd.DataFrame(list(conteo.items()),columns = ['Video','Número de dias trending'])
    conteo.sort_values()[0]
 
    return conteo

def getComentariosVideos(catalog, country, numerovideos, tag):
    video = -1000
    lista_sortear= lt.newList('ARRAY_LIST')
    for i in range(1, lt.size(catalog['videos'])+1):
        video = lt.getElement(catalog['videos'], i)
        if video["country"].lower().strip() == country.lower():
            lt.addLast(lista_sortear, video)    
    if lt.size(lista_sortear)==0:
        print('No hay referencias de videos de este pais')
    else:
        lista_comentarios = lt.newList('ARRAY_LIST')
        for k in range(1, lt.size(catalog['videos'])+1):
            video_comentarios = lt.getElement(catalog['videos'], k)
            tags = video["tags"]
            tags = str(tags)
            tag_escogido = str(tag)        
            if tags.find(tag_escogido)>=0:
                lt.addLast(lista_comentarios, video_comentarios)
        
        lista_sortear = sortVideosComents(lista_comentarios)
        if numerovideos <= lt.size(lista_comentarios):
            sublista = lt.subList(lista_comentarios, 1, numerovideos)
        else:
            print('No hay suficientes videos en la lista')
    return sublista


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByLikes(video1, video2):
    """ Devuelve verdadero (True) si los likes de video1 
    son menores que los del video2 Args: video1: informacion del 
    primer video que incluye su valor 'likes'"""
    return (int(video1['likes'])) > int((video2['likes']))

def cmpVideosByComments(video1, video2):
    """ Devuelve verdadero (True) si los likes de video1 
    son menores que los del video2 Args: video1: informacion del 
    primer video que incluye su valor 'likes'"""
    return (int(video1['comment_count'])) > int((video2['comment_count']))

# Funciones de ordenamiento

def sortVideosComents(lista):
    lista_sorteada = sa.sort(lista,cmpVideosByComments) 
    return lista_sorteada

def sortVideosLikes(lista):
    return sa.sort(lista,cmpVideosByLikes) 