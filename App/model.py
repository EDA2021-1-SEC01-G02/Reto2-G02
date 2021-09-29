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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa 
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo de obras

    Crea una lista vacia para guardar las obras

    Se crean indices para los mediums

    Retorna el catalogo inicializado.
    """
    catalog = {'books': None,
               'medium': None,
               }

    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareArtworks)

    catalog['medium'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=None)
 
    return catalog


# Funciones para agregar informacion al catalogo

def addArtWork(catalog, artwork):
    """
        Añade artworks
    """
    lt.addLast(catalog['artworks'], artwork)

def addMedium(mediums, artwork):
    """
    Añade mediums al mapa de Mediums y agrega artworks a una lista que tiene como valor
    """
    mediumName = artwork['Medium']
    if mp.contains(mediums, mediumName) == False:
        mp.put(mediums, mediumName, lt.newList('ARRAY_LIST', None))
    art = onlyMapValue(mediums,mediumName)
    lt.addLast(art, artwork)
    

# Funciones para creacion de datos

# Funciones de consulta

def onlyMapValue(map, key):
    """
    Se encarga de buscar el valor de un par, dado el mapa y la llave
    """
    pair =  mp.get(map,key)
    return me.getValue(pair)

def getMapSubList(map,medium, len):
    """
    Crea una sublista a partir de los elementos de una lista que hay almacenada en una pareja en el mapa.
    """
    lst = onlyMapValue(map, medium)
    new = lt.subList(lst,1,len)
    return new

# Funciones utilizadas para comparar elementos dentro de una lista
def compareArtworks(artwork1, artwork2):
    """
    Compara los codigos de los Artworks
    """
    id1 = artwork1['ObjectID'] 
    id2 = artwork2['ObjectID']
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMediumNames(name, medium):

    """
    Compara los nombres de los Mediums,
    devuelve 0 si son iguales, 
    1 si el primero es mayor y 
    -1 si es al reves
    """
    tagentry = me.getKey(medium)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1

def cmpArtworkByDate(artwork1,artwork2):
    
    """
    Si el primero es mayor, retorna True
    Si no, retorna False
    """

    date1 = artwork1['Date']
    date2 = artwork2['Date']
    if date1 == '':
        date1 =  0
    if date2 == '':
        date2 = 0
    if int(date1) < int(date2):
        return True
    else:
        return False

# Funciones de ordenamiento


def sortArtworksByDate(lst, cmpfunction):
    """
    Ordena una lista, dada su cmpfuntion como str
    """
    if 'cmpArtworksByDate' == cmpfunction:
        ms.sort(lst, cmpArtworkByDate)