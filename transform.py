#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pendulum
from pymongo import MongoClient


# Cargamos los datos en la base de datos.
def load_data(date, code, lat, lon, speed):
    client = MongoClient('localhost')
    db = client['transport']
    db_col = db['db_transport']
    db_col.insert_one({
        'Data_Time': date,
        'Code': code,
        'Latitude': lat,
        'Longitude': lon,
        'Speed': speed
    })


# Transformamos la zona horaria de Europe/France a local {America/Mexico_City}
def time_zone(data_list):
    data_time = data_list[2]
    data_time = pendulum.from_format(data_time, 'YYYY-M-D HH:mm:ss')
    data_time = data_time.in_timezone('America/Mexico_City')
    data_time = data_time.to_datetime_string()
    return data_time


# Leemos el archivo y lo recorremos reemplazando el tercer elemento de la lista.
def read_file(file_path):
    with open(file_path, 'r') as file:
        file_path = [line.split(',') for line in file.readlines()]
        for element in file_path[1:]:  # Omitimos la primera linea de la lista en la iteracion.
            new_time = time_zone(element)
            element[2] = new_time
            load_data(element[2], element[0], element[3], element[4], element[5])


# Leemos cada archivo dentro del Path.
def read_directory(path):
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = f"{path}\\{file}"
            read_file(file_path)
