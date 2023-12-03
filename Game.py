import pygame
import time
import random

pygame.init()

# Definir colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Configuración de la pantalla
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Juego de la Serpiente')

# Configuración del reloj
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

# Función para dibujar la serpiente en la pantalla
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

# Función para mostrar la puntuación en la pantalla
def Your_score(score):
    value = font_style.render("Puntuación: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Inicializar la posición de la serpiente
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Inicializar el cambio en la posición de la serpiente
    x1_change = 0
    y1_change = 0
    # Crea una lista vacía para almacenar las coordenadas de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Posición inicial de la manzana
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
    
        while game_close == True:
            dis.fill(black)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Verificar si la serpiente se sale de la pantalla
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Mover la serpiente
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Dibujar la manzana
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Añadir la cabeza de la serpiente a la lista
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Mantener el tamaño de la serpiente
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Verificar si la serpiente se muerde a sí misma
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Dibujar la serpiente
        our_snake(snake_block, snake_List)

        # Dibujar la puntuación
        Your_score(Length_of_snake - 1)

        # Actualizar la pantalla
        pygame.display.update()

        # Verificar si la serpiente alcanza la manzana
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Configurar la velocidad del juego
        clock.tick(snake_speed)

    pygame.quit()
    quit()
 
gameLoop()



