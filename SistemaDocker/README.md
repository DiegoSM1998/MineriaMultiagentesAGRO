##    Instrucciones
### 1º. Ejecutar docker-Desktop
### 2º. lanzar servidor: docker compose -f .\docker_compose.yml up 
(Desde el navegador puedes acceder a las tablas postgresqul en la dirección localhost:8080, debereas introducir los datos de acceso que estan disponibles en el archivo docker_compose.yml)
![Login](https://github.com/DiegoSM1998/MineriaMultiagentesAGRO/blob/main/SistemaDocker/login.png)
### Ahora puedes accedr a las funciones o modificarlas en los ".py" de cada carpeta, siendo estas:
###   1.- Subir datasets masivos a postgresql (Entrar en el fichero ./pythonSubirData y seguir instrucciones)
###   2.- Descargar datos a medida a traves de escraper y subirlos postgresql (Entrar en el fichero ./selenium y seguir instrucciones)
###   3.- Limpiar raw data que se encuentra en postgresql y volver a subirlos ya procesados (Entrar en el fichero ./pythonLimpiarData y seguir instrucciones)
###   4.- Comprobar la calidad de los datos de las tablas en la base de datos (Entrar en el fichero ./pythonCheckPandera y seguir instrucciones)
###   5.- Usar el modelo de regresión lineal (Entrar en el fichero ./modelo y seguir instrucciones)
(Una vez creadas las imagenes podras ejecutarlas e interactuar entre ellas gracias a que todas se comunican con la base de datos AGROdb)
_________________________________________________________________________________________________________________________________________________________________________

## Diagrama Arquitectura
![Diagrama](https://github.com/DiegoSM1998/MineriaMultiagentesAGRO/blob/main/SistemaDocker/diagrama.png)
