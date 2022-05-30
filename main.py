#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from download import *
from transform import *

# Inicializamos el Script.
if __name__ == '__main__':

    # Variables necesarias para ejecutar descarga_archivos
    fecha = input('Introduce la fecha : {dd/mm/aaaa} ')
    path = os.path.dirname(__file__)

    # Reformateamos la variable fecha para usarla como nombre de directorio.
    fecha_dir = fecha.split('/')
    fecha_dir = "{}-{}-{}".format(fecha_dir[2], fecha_dir[1], fecha_dir[0])
    download_folder = (path + '\\Descargas\\' + fecha_dir)

    # Invocamos a nuestras funciones!
    create_folder(download_folder)
    descargar_archivos(fecha, path, download_folder)
    read_directory(download_folder)
