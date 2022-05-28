#!/usr/bin/python
# -*- coding: utf-8 -*-

from download import descargar_archivos

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fecha = input('Introduce la fecha: dd/mm/aaaa: ')
    descargar_archivos(fecha)
