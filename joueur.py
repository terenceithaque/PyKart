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

        # global vitesse
        self.vitesse = 0  # Vitesse de déplacement initiale

        self.direction = 0  # Direction du véhicule

        self.vitesse_max = 5  # Vitesse de déplacement maximale
        self.acceleration = 0.1  # Taux d'accélération
        self.deceleration = 0.1  # Taux de décélération

        # self.vitesse = 5  # Vitesse de déplacement du joueur

    def avancer(self):
        "Faire avancer le joueur"
        # Si le joueur appuie sur la touche "flèche vers le haut":

        self.acceleration += 0.1
        self.vitesse = min(
            self.vitesse + self.acceleration, self.vitesse_max)
        print("self.vitesse :", self.vitesse)

        self.rect.y -= self.vitesse
        pygame.time.wait(100)

    def reculer(self):
        "Faire reculer le joueur"
        # Si le joueur appuie sur la touche "flèche vers le bas":
        # self.vitesse = 5
        # if key[pygame.K_DOWN]:
        # self.acceleration += 0.1
        self.vitesse = max(
            self.vitesse + self.acceleration, -self.vitesse_max)
        self.rect.y += self.vitesse
        pygame.time.wait(100)

    def get_events(self):
        list_events = pygame.event.get()
        return list_events

    def freiner(self):

        if self.vitesse > 0:  # Si la vitesse du kart est supérieure à 0
            # Réduire la vitesse jusqu'à ce qu'elle atteigne 0
            self.vitesse = max(self.vitesse - self.deceleration, 0)
            self.direction = -1  # Direction du véhicule
            print("self.direction", self.direction)
            pygame.time.wait(100)
            self.rect.y += self.direction

        elif self.vitesse < 0:
            # Augmenter la vitesse, car elle est négative
            self.vitesse = min(self.vitesse + self.deceleration, 0)
            self.direction = 1
            print("self.direction", self.direction)
            pygame.time.wait(100)
            self.rect.y += self.direction

        self.acceleration = 0.1  # Réinitialiser l'accélération
        self.direction = 0
        pygame.time.wait(100)

    def draw(self, screen, camera):

        screen.blit(self.image, camera.apply(self))
