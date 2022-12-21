### Para crear la imagen y lanzarla:
### docker build -t pandera .
### docker run -it pandera
_________________________________________________________________________________________________________________________________________________________________________
### Esta imagen te permitira comprobar la calidad de tus datos subidos en tablas en la base postgresql
### -Dockerfile recoge los parametros necesarios para crear la imagen con el codigo python y su respectivo entorno
### -checkDataPnadera.py es el codigo python donde se especifican las cualidades esperadas de los datos (podras modificarlo antes de crear la imagen, esta prepara para los datasets principales que usamos), el codigo tambien se encarga de mostrate las tablas disponibles en la base de datos y seleccionar cual quieres someter al examen de calidad.
