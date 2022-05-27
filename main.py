#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def descargar_archivos():
    # Preguntamos al usuario por la fecha.
    fecha = input("Introduce la Fecha (dd/mm/aaaa): ")

    # Obtenemos el directorios de destino raiz
    path = os.path.dirname(__file__)
    driver_path = Service(path + '\\chromedriver.exe')
    download_folder = (path + '\\Descargas')

    # Definimos las opciones para chrome, definir el directorio de descarga.
    prefs = {'download.default_directory': download_folder}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)

    # Definir las Chrome options
    driver = webdriver.Chrome(service=driver_path, options=options)

    # Ir GeoConnect, introcimos credenciales, iniciamos sesion.
    driver.get("http://201.144.109.78:8080/login.jsp?n=0")
    driver.find_element(By.NAME, 'Username').send_keys('15-SurDalias')
    driver.find_element(By.NAME, 'Password').send_keys('********')
    login_button = driver.find_element(By.NAME, 'Submit')
    login_button.click()

    # Diccionario con los valores de cada unidad. { 'Id':'Concesion' }
    lista_ids = {'532': '6284', '477': '4796', '419': '6236', '423': '6256', '398': '3523',
                 '408': '4677', '425': '6278', '397': '3522', '401': '4515', '453': '7388',
                 '524': '4660', '740': '6274', '418': '6234', '421': '6243', '522': '4653',
                 '486': '7409', '450': '7375', '461': '7440', '417': '6233', '460': '7435',
                 '531': '6237', '426': '6281', '752': '5139', '422': '6252', '443': '7008',
                 '429': '6285', '420': '6238', '763': '4680', '731': '7363', '404': '4553',
                 '427': '6282', '760': '5147', '411': '5122', '480': '6153', '479': '5123',
                 '399': '3536', '751': '5121', '753': '6163', '362': '7396', '296': '6183'}

    # Iteramos para formar cada link de Descarga. El formato es: data_boitier_7440_2022-05-25
    for key, value in lista_ids.items():
        driver.get(
            "http://201.144.109.78:8080/daily-file-export.jsp?v_id="
            + key + "&v_code=" + value + "&dr_date=" + fecha + "&sep=col")

    fecha = fecha.split('/')
    fecha = "{}-{}-{}".format(fecha[2], fecha[1], fecha[0])
    file_name = 'data_boitier_6183_{}.txt'.format(fecha)

    # Verificamos si existe el ultimo archivo que descargamos, de ser asi, cerramos el web Driver.
    while not os.path.exists(download_folder + '\\' + file_name):
        time.sleep(1)

    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    descargar_archivos()