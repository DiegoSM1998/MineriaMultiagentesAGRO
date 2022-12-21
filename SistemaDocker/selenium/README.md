### Para crear la imagen y lanzarla:
### docker build -t selenium .
### docker run -it selenium  

### Esta imagen te permitira ampliar la base de datos y subir las tablas directamente a postgresql
### -Dockerfile recoge los parametros necesarios para crear la imagen con el codigo python y su respectivo entorno
### -ScraperDBConsumoHogaresConsultas.py es el codigo python que usando selenium actua de scraper para bajar los datos de la pagina:"https://www.mapa.gob.es/app/consumo-en-hogares/consulta11.asp", cuenta con un formulario para indicar el periodo y comunidad autonoma del que quieres obtener los datos.

______________________________________________________________________________________________________________________________

Los siguientes programas no estan totalmente integrados en el sistema pero si que se usan por ejemplo para generar la base de datos ampliada, (pero conlleva una gran cantidad de tiempo ejecutarlos por completo)

-ScraperDBConsumoHogaresIterativo.py funciona tambien con selenium como scraper pero esta vez no se detiene con un periodo o comunidad si no que descarga de forma recursiva los datos de todas las comunidades y de todos los periodos, una vez indicado el año desde el que quieres obtener los datos.
-ScraperDBSuperalimentos.py sencillamente accede a una pagina web con una lista de super alimentos y extrae las claves para generar un txt en formma de lista.
