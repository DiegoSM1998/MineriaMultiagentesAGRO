
### Para crear la imagen y lanzarla:
### docker build -t model .
### docker run -it model

### Esta imagen permite aplicar un modelo de regresión lineal sobre una de la tablas ya procesadas ubicadas en postrgresql
### -Dockerfile recoge los parametros necesarios para crear la imagen con el codigo python y su respectivo entorno
### -linear_regression.py es el codigo python que ejecuta el modelo y que podremos modificar antes de crear la imagen 

![Regresión Lineal(ejemplo)](https://github.com/DiegoSM1998/MineriaMultiagentesAGRO/blob/main/SistemaDocker/modelo/Regresi%C3%B3n%20lineal.png)
