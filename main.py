# Script principal du jeu
import pygame
from pygame.camera import Camera
from pygame.draw import polygon
import random
import time
from joueur import *
from camera import *

pygame.init()  # Initialiser Pygame

screen = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu

pygame.display.set_caption("PyKart !")

chemin_image_joueur = "images/kart.png"


joueur = Joueur(chemin_image_joueur, 120, 110)

BRAKE_EVENT = pygame.USEREVENT + 1


def generer_terrain():
    "Générer le terrain"
    terrain = []  # Créer une liste pour contenir les données du terrain de jeu
    x = random.randint(100, 300)
    y1 = 0
    y2 = 600
    terrain.append((x, y1, y2))
    for i in range(100, 600):  # Générer le terrain
        # Valeur de pente au hasard pour créer des virages
        pente = random.randint(-5, 5)
        x += pente
        if x > 300:
            x = 300

        elif x < 100:
            x = 100

        y1 += random.randint(1, 5)
        y2 -= random.randint(1, 5)

        terrain.append((x, y1, y2))

    return terrain


def dessiner_terrain(terrain):
    "Dessiner le terrain à l'écran"

    screen.fill((0, 255, 0))

    for i in range(len(terrain) - 1):
        x1, y1, y2 = terrain[i]
        x2, y3, y4 = terrain[i+1]

        # Dessiner la route
        pygame.draw.polygon(screen, (192, 192, 192), [
                            (x1, y1), (x2, y3), (x2, y4), (x1, y2)])

        # Dessiner les lignes blanches qui délimitent la route
        pygame.draw.lines(screen, (255, 255, 255),
                          False, [(x1, y1), (x2, y3)], 1)
        pygame.draw.lines(screen, (255, 255, 255),
                          False, [(x1, y2), (x2, y4)], 1)


def dessiner_ligne_depart(circuit):
    "Dessiner la ligne de départ"
    if len(circuit) > 0:
        x1, _, _ = circuit[0]
        x2, _, _ = circuit[-1]
        pygame.draw.line(screen, (255, 255, 255), (x1, 0),
                         (x1, 600), 5)  # Vertical starting line
        pygame.draw.line(screen, (255, 255, 255), (x2, 0),
                         (x2, 600), 5)  # Vertical ending line


seed = time.time()
random.seed(seed)
circuit = generer_terrain()
dessiner_terrain(circuit)
dessiner_ligne_depart(circuit)
pygame.display.update()

pygame.display.update()

camera = Camera(800, 600)


running = True  # Le jeu est-il en cours d'exécution ?


while running:

    keys = pygame.key.get_pressed()  # Obtenir toutes les touches pressées par le joueur

    # print("Etat touche haut :", keys[pygame.K_UP])
    # print("Etat touche bas :", keys[pygame.K_DOWN])

    if keys[pygame.K_UP]:  # Si le joueur appuie sur la touche 'flèche vers le haut'
        joueur.avancer()  # Le kart du joueur avance

    elif keys[pygame.K_DOWN]:  # Si le joueur appuie sur la touche 'flèche vers le bas'
        joueur.reculer()  # Le kart du joueur recule

    else:  # Sinon
        joueur.freiner()  # Le kart du joueur freine

    # Mettre à jour la position de la caméra avec le joueur comme cible
    camera.update(joueur)

    joueur.draw(screen, camera)

    for evenement in pygame.event.get():  # Pour chaque évènement intercepté durant l'exécution du jeu
        if evenement.type == pygame.QUIT:  # Si le joueur veut quitter le jeu
            running = False  # Terminer cette boucle

    pygame.display.flip()
