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
 """

import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    return model.newCatalog()

# Funciones para la carga de datos
def loadData(catalog):
    loadArtists(catalog)
    loadArtWorks(catalog)

def loadArtWorks(catalog):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding = 'utf-8'))
    for artwork in input_file:
        model.addArtWork(catalog, artwork)
        model.addMedium(catalog['medium'], artwork)
        model.addNationality(catalog["nationality"], catalog["artists"], artwork)

def loadArtists(catalog):
    artistsfile = cf.data_dir + "MoMA/Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistsfile, encoding= "utf-8"))
    for artist in input_file:
        model.addArtist(catalog,artist)

# Funciones de ordenamiento

def sortArtworksByDate(map, key):
    lst = model.onlyMapValue(map, key)
    model.sortArtworksByDate(lst, 'cmpArtworksByDate')

# Funciones de consulta sobre el catálogo

def masAntic(map, len, medium):
    sortArtworksByDate(map, medium)
    lst = model.getMapSubList(map,medium, len)
    for a in lst['elements']:
        print(a)