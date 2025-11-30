#1 IMPORTAR LOS MODULOS NECESARIOS
import pygame #--> Libreria que nos permite la creacion de juegos 2D
import math #--> Libreria que nos permite controlar ejercicios matematicos
import random #--> Libreria para generar numeros aletatoris, para mezcla aleatoria etc
import sys #--> Libreria para interactuar con el entorno de ejecucion y con las variables de entorno del sistema
from pygame import mixer #--> Libreria para manejar el audio en juegosz,y reproducir efectos de sonido y música de fondo.

#INICIO DEL JUEGO

try:
    #2 INICIAR PYGAME
    pygame.init() #--> Abre la ventana
    mixer.init() #--> Inicia el modulo mixer (sonidos)
    mixer.
    ancho = 640 #--> Ancho de ventana
    alto = 480 #--> Alto de ventana

    ventana = pygame.display.set_mode((ancho,alto)) #--> Configuracion de tamaño de ventana
    pygame.display.set_caption("Los Guardianes de la fracciones") #--> Titulo de ventana

    #3 COLORES PARA INTERFAZ Y MENÚS
    BLANCO = (255, 255, 255)      #--> Textos principales, elementos de UI
    NEGRO = (0, 0, 0)             #--> Fondos de texto, contornos
    GRIS = (128, 128, 128)        #--> Plataformas de suelo, elementos neutros

    # COLORES PARA BOTONES Y INTERACCIÓN
    VERDE_OSCURO = (0, 128, 0)    #--> Estado NORMAL de botones (no presionados)
    VERDE = (0, 255, 0)           #--> Estado HOVER de botones (mouse encima)
    ROJO = (255, 0, 0)            #--> Errores, advertencias, personaje 1

    # COLORES PARA PERSONAJES JUGABLES
    ROJO = (255, 0, 0)            #--> PERSONAJE 1: "MATEMATICUS"
    AZUL = (0, 0, 255)            #--> PERSONAJE 2: "CALCULIN"  
    VERDE = (0, 255, 0)           #--> PERSONAJE 3: "NUMERIX"
    MORADO = (128, 0, 128)        #--> PERSONAJE 4: "MATHERO"

    # COLORES PARA NIVELES Y PLATAFORMAS
    NARANJA = (255, 165, 0)       #--> PLATAFORMAS del NIVEL 1 (Principiante)
    VERDE = (0, 255, 0)           #--> PLATAFORMAS del NIVEL 2 (Intermedio)  
    NARANJA = (255, 165, 0)       #--> PLATAFORMAS del NIVEL 3 (Avanzado)
    MORADO = (128, 0, 128)        #--> PLATAFORMAS del NIVEL 4 (Experto)

    # COLORES PARA FONDOS DE NIVELES
    CIELO = (135, 206, 235)       #--> FONDO del NIVEL 1 (azul cielo - principiante)
    VERDE = (0, 255, 0)           #--> FONDO del NIVEL 2 (verde - intermedio)
    NARANJA = (255, 165, 0)       #--> FONDO del NIVEL 3 (naranja - avanzado)
    MORADO = (128, 0, 128)        #--> FONDO del NIVEL 4 (morado - experto)

    # COLORES PARA ELEMENTOS ESPECIALES
    AMARILLO = (255, 255, 0)      #--> META (objetivo final), títulos importantes
    DORADO = (255, 215, 0)        #--> Indicadores de selección, elementos premium
    AZUL_OSCURO = (0, 0, 128)     #--> Botones de selección, paneles de información
    ROSA = (255, 192, 203)        #--> Color de respaldo/alternativo

    #4 ESTADOS DEL JUEGO (MÁQUINA DE ESTADOS)
    MENU = 0               #--> Pantalla principal del menú
    SELECCION_PERSONAJE = 1 #--> Pantalla para elegir personaje jugable
    JUGANDO = 2            #--> Pantalla de juego principal con plataformas
    PREGUNTA_FRACCION = 3  #--> Pantalla que muestra preguntas matemáticas
    GANADO = 4             #--> Pantalla de victoria/nivel completado
    SELECCION_NIVEL = 5    #--> Pantalla para elegir nivel de dificultad

    #5 VARIABLES GLOBALES PARA CONTROL DE AUDIO Y RECURSOS
    musica_actual = ""        #--> Guarda qué música se está reproduciendo actualmente
    sonidos_cargados = False  #--> Bandera que indica si los efectos de sonido se cargaron bien
    imagenes_cargadas = False #--> Bandera que indica si las imágenes se cargaron correctamente

    # Configuracion del jugador
    # Haremos uso de clases para empaquetar datos-- Creamos clase = Nuevo objeto
    
    # Clase del jugador
    class Jugador:
        def __init__(self): # Self -> Variable que permite acceder a sus propiedades
            self.ancho = 50
            self.alto = 50 
            self.x = 100 # Posicion en eje x
            self.y = 200 # Posicion en eje y
            self.velocidad_x = 0
            self.velocidad_y = 0
            self