#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pendulum


def time_zone(data_list):
    data_time = data_list[2]
    data_time = pendulum.from_format(data_time, 'YYYY-M-D HH:mm:ss')
    data_time = data_time.in_timezone('America/Mexico_City')
    data_time = data_time.to_datetime_string()
    return data_time


def read_file(file_path):
    with open(file_path, 'r') as file:
        file_path = [line.split(',') for line in file.readlines()]
        for element in file_path[1:]:  # Omitimos la primera linea de la lista en la iteracion.
            new_time = time_zone(element)
            element[2] = new_time
            print(element)


def read_directory(path):
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = f"{path}\\{file}"
            read_file(file_path)
