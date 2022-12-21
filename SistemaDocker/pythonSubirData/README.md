### Para crear la imagen y lanzarla:
### docker build -t subirdata .
### docker run subirdata

### Esta imagen se encarga de subir las bases de datos más grandes a postgresql, ya que contamos con scrapers que son capaces de recolectar una gran cantidad de datos, no hay necesidad de ejecutarlos cada vez que queramos usar esos datos, por ello hemos decidido subir los datasets principales de esta manera.

### -Dockerfile recoge los parametros necesarios para crear la imagen con el codigo python y su respectivo entorno
### -subirData.py es el codigo que se encarga de transformar los txt en csv y subirlos a postgresql (Cualquier dataset que queramos añadir en el futuro deberemos incluirlo en la carpeta ./Data para poder lanzarlo con este codigo)
