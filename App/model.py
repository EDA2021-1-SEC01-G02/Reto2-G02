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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

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
    lt.addLast(catalog['artworks'], artwork)
    artists = artwork['ConstituentID'].split(',')
    artworktitle = artwork['Title']

    for artist in artists:
        addArtWorkArtist(catalog, artist.strip() , artworktitle)

def addArtWorkArtist(catalog, artistname, artwork):
    
    artists = catalog['artists']
    posArtist = lt.isPresent(artists, artistname)
    if posArtist > 0:
        artist = lt.getElement(artists, posArtist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists, artist)
    artistname = artist['name']

    lt.addLast(artist['artworks'], artwork)

def newArtist(name):
    
    artist = {
        'name' : "",
        'artworks' : None,
        'info' : None,
            }
    artist['name'] = name
    artist['artworks'] = lt.newList('ARRAY_LIST')
    artist['info'] = 'x'
    return artist






# Funciones para creacion de datos


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareArtworks(artwork1, artwork2):
    """
    Compara dos ids de dos libros
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
    tagentry = me.getKey(medium)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1
# Funciones de ordenamiento
