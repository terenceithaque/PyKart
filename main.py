# Script principal du jeu
import pygame
import random
import time

pygame.init()  # Initialiser Pygame

screen = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu

pygame.display.set_caption("PyKart !")


def generer_terrain():
    "Générer le terrain"
    terrain = []  # Créer une liste pour contenir les données du terrain de jeu
    x = 0
    y = random.randint(400, 500)
    terrain.append(y)
    for i in range(1, 800):  # Générer le terrain
        # Valeur de pente au hasard pour créer des virages
        pente = random.randint(-5, 5)
        y += pente
        if y > 600:
            y = 600
        elif y < 400:
            y = 400

        terrain.append(y)

    return terrain


def dessiner_terrain(terrain):
    "Dessiner le terrain à l'écran"
    for i in range(799):  # Dessiner le terrain
        pygame.draw.line(screen, (192, 192, 192),
                         (i, terrain[i]), (i+1, terrain[i+1]))


def dessiner_ligne_depart():
    "Dessiner la ligne de départ"
    pygame.draw.line(screen, (255, 255, 255), (0, 500), (800, 500), 5)


seed = time.time()
random.seed(seed)
terrain = generer_terrain()
dessiner_terrain(terrain)
dessiner_ligne_depart()
pygame.display.update()

pygame.display.update()


running = True  # Le jeu est-il en cours d'exécution ?

while running:
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté durant l'exécution du jeu
        if evenement.type == pygame.QUIT:  # Si le joueur veut quitter le jeu
            running = False  # Terminer cette boucle

    pygame.display.flip()
