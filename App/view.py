﻿"""
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

import controller
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Las n obras más antiguas para un medio específico")
    print("3- Consultar el numero de obras de una nacionalidad")

catalog = None

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        num_artworks = lt.size(catalog['artworks'])
        print('Artworks cargados: ' + str(num_artworks))
        num_artists = lt.size(catalog["artists"])
        print("Artistas cargados: " + str(num_artists))

    elif int(inputs[0]) == 2:
        medium =  input('Ingrese el medio: \n')
        len = int(input('Ingrese el numero de obras mas antiguas a cargar:\n'))
        mapMedium = catalog['medium']
        print('Las %s obras mas antiguas hechas en la modalidad %s son: \n' %(len, medium))
        controller.masAntic(mapMedium, len, medium)

    #Requerimiento 4
    elif int(inputs[0]) == 3:
        nacionalidad = input("Digite la nacionalidad a buscar: ").capitalize()
        resultado = controller.natRank(catalog["nationality"],nacionalidad)
        if resultado == None:
            print("No se encontro la nacionalidad especificada.")
        else:
            print("La nacionalidad "+nacionalidad+" tiene un total de obras de "+str(resultado))


    else:
        sys.exit(0)
sys.exit(0)