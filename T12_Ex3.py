import pygame
import sys

class Pong:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()

        # Configuración de la pantalla
        self.ANCHURA = 800 # Anchura de la pantalla
        self.ALTO = 600 # Altura de la pantalla
        self.screen = pygame.display.set_mode((self.ANCHURA, self.ALTO)) # Crea una pantalla de ANCHURA x ALTO
        pygame.display.set_caption("Pong") # Asigna un títul a la pantalla

        # Colores
        self.BLANCO = (255, 255, 255) # Color blanco
        self.NEGRO = (0, 0, 0) # Color negro

        # Configuración de los jugadores y la pelota
        self.AMPLE_JUGADOR = 10 # pixels amplada del jugador
        self.ALÇADA_JUGADOR = 100 # pixels altura del jugador
        self.VELOCITAT_JUGADOR = 5
        self.RADI_PILOTA = 10 
        self.VELOCITAT_PILOTA_X = 5
        self.VELOCITAT_PILOTA_Y = 5

        # Posiciones iniciales
        self.jugador1_x = 50 # Posició inicial del jugador 1
        self.jugador1_y = self.ALTO // 2 - self.ALÇADA_JUGADOR // 2 # Posició inicial del jugador 1
        self.jugador2_x = self.ANCHURA - 50 - self.AMPLE_JUGADOR  # Posició inicial del jugador 2
        self.jugador2_y = self.ALTO // 2 - self.ALÇADA_JUGADOR // 2 # Posició inicial del jugador 2
        self.pilota_x = self.ANCHURA // 2  # Posició inicial de la pilota
        self.pilota_y = self.ALTO // 2 # Posició inicial de la pilota
        self.vel_pilota_x = self.VELOCITAT_PILOTA_X 
        self.vel_pilota_y = self.VELOCITAT_PILOTA_Y

    def moure_pilota(self):
        self.pilota_x += self.vel_pilota_x # Mou la pilota en el eix x
        self.pilota_y += self.vel_pilota_y # Mou la pilota en el eix y
        
        # Col·lisions amb els marges verticals
        if self.pilota_y <= 0 or self.pilota_y >= self.ALTO - self.RADI_PILOTA: # Si la pilota toca el marge superior o inferior, canvia el sentit
            self.vel_pilota_y = -self.vel_pilota_y # Canvia el sentit en el eix y
        
        # Col·lisions amb els jugadors
        if (self.pilota_x <= self.jugador1_x + self.AMPLE_JUGADOR and # Si la pilota toca el jugador 1
            self.pilota_y >= self.jugador1_y and # Si la pilota toca el jugador 1 superior o inferior,
            self.pilota_y <= self.jugador1_y + self.ALÇADA_JUGADOR): # Canvia el sentit en el eix y
            self.vel_pilota_x = -self.vel_pilota_x # Canvia el sentit en el eix x
        
        if (self.pilota_x >= self.jugador2_x - self.RADI_PILOTA and # Si la pilota toca el jugador 2
            self.pilota_y >= self.jugador2_y and # Si la pilota toca el jugador 2 superior o inferior,
            self.pilota_y <= self.jugador2_y + self.ALÇADA_JUGADOR): #  Canvia el sentit en el eix y
            self.vel_pilota_x = -self.vel_pilota_x # Canvia el sentit en el eix x
        
        # Punt marcat
        if self.pilota_x < 0 or self.pilota_x > self.ANCHURA: # Si la pilota toca el marge esquerra o dreta, reinicia
            self.reiniciar_pilota() # Reinicia la pilota

    def reiniciar_pilota(self):
        self.pilota_x = self.ANCHURA // 2 # Posició inicial de la pilota en x
        self.pilota_y = self.ALTO // 2 # Posició inicial de la pilota en y
        self.vel_pilota_x = self.VELOCITAT_PILOTA_X # Canvia el sentit en el eix x
        self.vel_pilota_y = self.VELOCITAT_PILOTA_Y # Canvia el sentit en el eix y

    def gestionar_events(self): 
        for event in pygame.event.get(): # Gestiona los eventos de la pantalla
            if event.type == pygame.QUIT: # Si es pitja el botó de sortir, atura el programa
                pygame.quit() 
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.jugador1_y > 0: # Mou el jugador 1 en el eix y
            self.jugador1_y -= self.VELOCITAT_JUGADOR
        if keys[pygame.K_s] and self.jugador1_y < self.ALTO - self.ALÇADA_JUGADOR: # Mou el jugador 1 en el eix y
            self.jugador1_y += self.VELOCITAT_JUGADOR 
        if keys[pygame.K_UP] and self.jugador2_y > 0:# Mou el jugador 2 en el eix y
            self.jugador2_y -= self.VELOCITAT_JUGADOR
        if keys[pygame.K_DOWN] and self.jugador2_y < self.ALTO - self.ALÇADA_JUGADOR: # Mou el jugador 2 en el eix y
            self.jugador2_y += self.VELOCITAT_JUGADOR

    def dibuixar_elements(self):
        self.screen.fill(self.NEGRO)
        pygame.draw.rect(self.screen, self.BLANCO, (self.jugador1_x, self.jugador1_y, self.AMPLE_JUGADOR, self.ALÇADA_JUGADOR)) # Dibuixa el jugador 1
        pygame.draw.rect(self.screen, self.BLANCO, (self.jugador2_x, self.jugador2_y, self.AMPLE_JUGADOR, self.ALÇADA_JUGADOR)) # Dibuixa el jugador 2
        pygame.draw.circle(self.screen, self.BLANCO, (self.pilota_x, self.pilota_y), self.RADI_PILOTA) # Dibuixa la pilota

    def executar_joc(self): # Funció principal del joc
        while True:
            self.gestionar_events()# Gestiona els events
            self.moure_pilota() # Mou la pilota
            self.dibuixar_elements() # Dibuixa els elements
            pygame.display.flip() # Refresca la pantalla
            pygame.time.delay(30)  # Petit retard per controlar la velocitat del joc

def pex3():
    pong = Pong()
    pong.executar_joc()
