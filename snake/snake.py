
import pygame
import time
import random


pygame.init()


blanco = (255, 255, 255)
amarillo = (255, 255, 102)
verde = (0, 255, 0)
negro = (0, 0, 0)
rojo = (213, 50, 80)
azul = (50, 153, 213)
verde_claro = (0, 128, 0)


ancho = 600
alto = 600


pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Serpiente')


reloj = pygame.time.Clock()


tamaño_segmento = 10


fuente = pygame.font.SysFont("bahnschrift", 25)


def mostrar_puntaje(puntaje):
    valor = fuente.render("Puntaje: " + str(puntaje), True, blanco)
    pantalla.blit(valor, [0, 0])


def dibujar_serpiente(tamaño_segmento, lista_segmentos):
    for segmento in lista_segmentos:
        pygame.draw.rect(pantalla, verde_claro, [segmento[0], segmento[1], tamaño_segmento, tamaño_segmento])


def juego():
    fin_juego = False
    perdio = False

    
    x1 = ancho / 2
    y1 = alto / 2

    
    x1_cambio = 0
    y1_cambio = 0

    
    lista_segmentos = []
    longitud_serpiente = 1

    
    comida_x = round(random.randrange(0, ancho - tamaño_segmento) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_segmento) / 10.0) * 10.0

    
    while not fin_juego:

        while perdio:
            pantalla.fill(azul)
            mensaje = fuente.render("Perdiste! Pulsa C para jugar de nuevo o Q para salir", True, rojo)
            pantalla.blit(mensaje, [ancho / 6, alto / 3])
            mostrar_puntaje(longitud_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fin_juego = True
                    perdio = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fin_juego = True
                        perdio = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_segmento
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_segmento
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_segmento
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_segmento
                    x1_cambio = 0

        
        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            perdio = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)

        
        pygame.draw.rect(pantalla, amarillo, [comida_x, comida_y, tamaño_segmento, tamaño_segmento])

        
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_segmentos.append(cabeza_serpiente)

        if len(lista_segmentos) > longitud_serpiente:
            del lista_segmentos[0]

        
        for segmento in lista_segmentos[:-1]:
            if segmento == cabeza_serpiente:
                perdio = True

        dibujar_serpiente(tamaño_segmento, lista_segmentos)
        mostrar_puntaje(longitud_serpiente - 1)

        pygame.display.update()

        
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_segmento) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_segmento) / 10.0) * 10.0
            longitud_serpiente += 1

        
        reloj.tick(15)

    pygame.quit()
    quit()

juego()