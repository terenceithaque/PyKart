# Script principal du jeu
import pygame
import random
import time

pygame.init()  # Initialiser Pygame

screen = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu

pygame.display.set_caption("PyKart !")

seed = time.time()
random.seed(seed)
print(seed)

terrain = []  # Créer une liste pour contenir les données du terrain de jeu

for i in range(800):  # Générer le terrain
    terrain.append(random.randint(0, 600))

for i in range(800):  # Dessiner le terrain
    pygame.draw.line(screen, (0, 255, 0), (i, 600), (i, 600 - terrain[i]))


pygame.display.update()


running = True  # Le jeu est-il en cours d'exécution ?

while running:
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté durant l'exécution du jeu
        if evenement.type == pygame.QUIT:  # Si le joueur veut quitter le jeu
            running = False  # Terminer cette boucle

    pygame.display.flip()
