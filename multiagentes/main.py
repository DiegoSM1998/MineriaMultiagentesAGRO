import pygame
import random

# Definimos algunas constantes para controlar el tamaño de la ventana y la serpiente
ANCHO_VENTANA = 400
ALTO_VENTANA = 400
TAMANO_SERPIENTE = 20

# Inicializamos Pygame y creamos la ventana del juego
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Juego de la serpiente')

# Definimos algunas variables para controlar la posición y dirección de la serpiente
posicion_x = ANCHO_VENTANA // 2
posicion_y = ALTO_VENTANA // 2
direccion_x = 0
direccion_y = -TAMANO_SERPIENTE

# Creamos una lista para almacenar los bloques de la serpiente
bloques_serpiente = []

# Creamos una variable para almacenar la posición de la comida
posicion_comida_x = random.randint(0, ANCHO_VENTANA - TAMANO_SERPIENTE)
posicion_comida_y = random.randint(0, ALTO_VENTANA - TAMANO_SERPIENTE)

# Creamos una variable para controlar si el juego ha terminado o no
juego_terminado = False

# Creamos un bucle principal para actualizar el juego
while not juego_terminado:
    # Recorremos todos los eventos de Pygame
    for evento in pygame.event.get():
        # Si se ha pulsado el botón de cierre de la ventana, finalizamos el juego
        if evento.type == pygame.QUIT:
            juego_terminado = True
        # Si se ha pulsado alguna tecla, cambiamos la dirección de la serpiente
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                direccion_x = -TAMANO_SERPIENTE
                direccion_y = 0
            elif evento.key == pygame.K_RIGHT:
                direccion_x = TAMANO_SERPIENTE
                direccion_y = 0
            elif evento.key == pygame.K_UP:
                direccion_x = 0
                direccion_y = -TAMANO_SERPIENTE
            elif evento.key == pygame.K_DOWN:
                direccion_x = 0
                direccion_y = TAMANO_SERPIENTE
    # Actualizamos la posición de la serpiente
    posicion_x += direccion_x
    posicion_y += direccion_y

    # Comprobamos si la serpiente ha comido la comida
    if posicion_x == posicion_comida_x and posicion_y == posicion_comida_y:
        # Si ha comido la comida, añadimos un nuevo bloque a la serpiente y generamos una nueva posición para la comida
        bloques_serpiente.append((posicion_x, posicion_y))
        posicion_comida_x = random.randint(0, ANCHO_VENTANA - TAMANO_SERPIENTE)
        posicion_comida_y = random.randint(0, ALTO_VENTANA - TAMANO_SERPIENTE)
    else:
        # Si no ha comido la comida, eliminamos el último bloque de la serpiente
        #bloques_serpiente.pop(0)
        bloques_serpiente.append((posicion_x, posicion_y))

    # Dibujamos la ventana de fondo
    ventana.fill((0, 0, 0))

    # Dibujamos la serpiente
    for bloque in bloques_serpiente:
        pygame.draw.rect(ventana, (0, 255, 0), (bloque[0], bloque[1], TAMANO_SERPIENTE, TAMANO_SERPIENTE))

    # Dibujamos la comida
    pygame.draw.rect(ventana, (255, 0, 0), (posicion_comida_x, posicion_comida_y, TAMANO_SERPIENTE, TAMANO_SERPIENTE))

    # Actualizamos la pantalla
    pygame.display.update()

# Cerramos Pygame una vez terminado el juego
pygame.quit()