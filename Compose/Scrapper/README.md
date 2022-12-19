  1. Ejecutamos el siguiente comando para poder crear un volumen compartido:
   ### docker volume create vcompartido
  2. Para crear una imagen con un script de python, ejecutamos el siguiente comando dentro de la carpeta con el dockerfile: 
  ### docker build -f Dockerfile.txt -t scrapper .
  3. Finalmente, el último comando nos lanza un docker con la imagen que hemos formado anteriormente, si nos fijamos en el contenido del volumen compartido cuando se ejecute el script, podremos ver que dentro tenemos el csv generado por el scrapper:  
   ### docker run -it -v vcompartido:/data/ scrapper
