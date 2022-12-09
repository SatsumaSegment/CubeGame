import pygame

class Player:

    def __init__(self, screen, color, x, y, w, h):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        self.this = pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.w, self.h])
    
    def update(self, x, y):
        self.x = x
        self.y = y

    def collision(self, other):
        return self.this.colliderect(other)


class Enemy:

    def __init__(self, screen, color, x, y, w, h):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.left = False
        self.right = True
    
    def draw(self):
        self.this = pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.w, self.h])

    def direction(self):
        if self.left:
            self.x -= 2
        elif self.right:
            self.x += 2


class Food:

    def __init__(self, screen, color, x, y, w, h):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        self.this = pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.w, self.h])
