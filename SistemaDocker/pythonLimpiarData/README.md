### Para crear la imagen y lanzarla:
### docker build -t limpiardata .
### docker run -it limpiardata
_________________________________________________________________________________________________________________________________________________________________________
### Esta imagen te permitira procesar de las tablas de la base de datos y volver a subirlas.
### -Dockerfile recoge los parametros necesarios para crear la imagen con el codigo python y su respectivo entorno
### -checkDataPnadera.py es el codigo python donde se especifica como limpiar los raw data usando pandas (podras modificarlo antes de crear la imagen, esta prepara para el formato de los datasets principales que usamos), el codigo tambien se encarga de mostrate las tablas disponibles en la base de datos y seleccionar cual quieres procesar.
