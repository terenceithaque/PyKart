# Caméra qui suit le joueur
import pygame  # Importer pygame


class Camera:
    "Caméra qui suit le joueur"

    def __init__(self, largeur, hauteur):
        self.camera = pygame.Rect(0, 0, largeur, hauteur)
        self.largeur = largeur
        self.hauteur = hauteur

    def apply(self, entite):
        "Changer la position de la caméra en fonction de l'entité cible"
        return entite.rect.move(self.camera.topleft)

    def update(self, cible):
        x = -cible.rect.x + int(self.largeur / 2)
        y = -cible.rect.y + int(self.hauteur / 2)

        # Limiter le scrolling à la taille de la carte
        x = min(0, x)  # limite gauche
        y = min(0, y)  # limite supérieure
        x = max(-(self.largeur * 2 - self.largeur), x)
        y = max(-(self.hauteur * 2 - self.hauteur), y)

        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)
