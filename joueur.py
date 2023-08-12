# Joueur
import pygame


class Joueur(pygame.sprite.Sprite):
    "Joueur"

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)  # Charger l'image du joueur
        # Redimentionner l'image du joueur
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = x  # Position x du joueur

        self.rect.y = y  # Position y du joueur

        global vitesse
        vitesse = 5  # Vitesse de déplacement du joueur

        # self.vitesse = 5  # Vitesse de déplacement du joueur

    def avancer(self, key):
        "Faire avancer le joueur"
        # Si le joueur appuie sur la touche "flèche vers le haut":
        global vitesse
        vitesse = 5
        if key[pygame.K_UP]:
            self.rect.y -= vitesse
            pygame.time.wait(10)

    def reculer(self, key):
        "Faire reculer le joueur"
        # Si le joueur appuie sur la touche "flèche vers le bas":
        # self.vitesse = 5
        if key[pygame.K_DOWN]:
            self.rect.y += vitesse
            pygame.time.wait(10)

    def freiner(self, key, event):
        "Freiner"
        # Si le joueur n'appuie pas sur les touches pour avancer ou reculer
        if not key[pygame.K_UP] or not key[pygame.K_DOWN]:

            pygame.time.set_timer(event, 1000)

            for event in pygame.event.get():
                if event.type == event:
                    global vitesse
                    vitesse = vitesse - 1
                    if vitesse < 0:
                        vitesse = 0

            # pygame.time.wait(100)

    def draw(self, screen):

        screen.blit(self.image, (self.rect.x, self.rect.y))
