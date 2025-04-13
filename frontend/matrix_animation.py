# frontend/matrix_animation.py
import pygame
import random

WIDTH, HEIGHT = 640, 480

class MatrixAnimation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Matrix Gesture Animation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Consolas', 20)
        self.columns = [0] * (WIDTH // 20)
        self.running = True
        self.effect = None

    def update_effect(self, gesture):
        self.effect = gesture

    def draw_matrix(self):
        self.screen.fill((0, 0, 0))
        for i in range(len(self.columns)):
            char = chr(random.randint(33, 126))
            green = (0, 255, 0)
            label = self.font.render(char, True, green)
            self.screen.blit(label, (i * 20, self.columns[i] * 20))
            self.columns[i] += 1
            if self.columns[i] * 20 > HEIGHT or random.random() > 0.95:
                self.columns[i] = 0

    def apply_effects(self):
        if self.effect == "point":
            self.columns = [c + 1 for c in self.columns]
        elif self.effect == "peace":
            self.columns = [random.randint(0, 10) for _ in self.columns]
        elif self.effect == "swipe":
            self.columns = self.columns[1:] + [0]
        elif self.effect == "thumbs_up":
            self.screen.fill((0, 255, 0))  # Matrix glow
        elif self.effect == "fist":
            self.columns = [0] * len(self.columns)  # Clear

    def run(self, gesture):
        self.apply_effects()
        self.draw_matrix()
        pygame.display.update()
        self.clock.tick(30)
