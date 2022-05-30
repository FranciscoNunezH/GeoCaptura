# GeoCaptura { Extract, Transform, Load }

<img src="https://github.com/FranciscoNunezH/GeoCaptura/blob/main/scr/Geoconnect%20%20Image.jpg" width="1200">

<h3 align="left"> Background: </h3>
<p align="left"> Tenemos una Web. <br>
Esta web fue desarrollada por un tercero, allá por el 2003 cuyo objetivo <br>
era ( y sigue siendo ) es el monitoreo de los intinerarios de trabajo de las <br>
diferentes rutas de transporte publico de la ciudad. </p>
 
<h3 align="left"> Extract: </h3>
<p align="left"> La Pagina GeoConnect, nos permite descargar por cada unidad <br>
para cada dia de operacion un reporte en formato .txt. <br>
Hay que cargar la pagina, seleccionando la fecha y la unidad, asi como navegar <br>
A traves de una serie de opciones, para llegar al apartado donde descargamos <br>
Es necesario hacer esto para cada unidad. <br>
</p>
<img src="https://github.com/FranciscoNunezH/GeoCaptura/blob/main/scr/Descarga%20Manual.gif?raw=true">
<p align="left"> Usando "Selenium", optimizamos la descarga de los archivos. <br>
<img src="https://github.com/FranciscoNunezH/GeoCaptura/blob/main/scr/Auto%20Descarga.gif?raw=true">
 
<h3 align="left"> Transform: </h3>
<p align="left"> Los archivos de texto que descargamos anteriormente <br>
En promedio, cuentan con 1800 lineas de información por cada unidad ( total de 39).<br>
Cada linea contiene:

- Codigo de Unidad [ Concesion ]
- Codigo de Operador
- Fecha y Hora [ En Zona Horaria GTM ]
- Latitud
- Longitud
- Velocidad
- I/O
- Validador
 
Necesitamos, limpiar la data, solo nos interesa:
 
- Codigo de Unidad ---> Para identificar de que unidad se trata.
- Fecha y Hora ---> Transformada a Zona horaria Local. [ MX ]
- Latitud y Longitud ---> Transformar coordenadas Geograficas a "human-readable address"
- Velocidad

</p>
<img src="https://github.com/FranciscoNunezH/GeoCaptura/blob/main/scr/Data.jpg">

 
 
<br>
<h3 align="left"> Load {MongoDB}: </h3>
<p align="left"> Cargamos la información ya transformada, a nuestra base de datos. <br>
</p>

<br>
<img src="https://github.com/FranciscoNunezH/GeoCaptura/blob/main/scr/Exito.png?raw=true">
<img src="https://github.com/FranciscoNunezH/GeoCaptura/blob/main/scr/DataDase.png?raw=true">
 
 <em> Sigo trabajando en esta pagina... :page_with_curl: </em>
 

