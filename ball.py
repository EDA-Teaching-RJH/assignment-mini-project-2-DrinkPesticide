import math
import random
import pygame

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.mass = self.radius * 0.1

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def bounce_walls(self, screen_width, screen_height):
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.vx = -self.vx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.vy = -self.vy

    def collide(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < self.radius + other.radius:
            angle = math.atan2(dy, dx)
            sin = math.sin(angle)
            cos = math.cos(angle)

            # Rotate velocity vectors
            vx1 = self.vx * cos + self.vy * sin
            vy1 = self.vy * cos - self.vx * sin
            vx2 = other.vx * cos + other.vy * sin
            vy2 = other.vy * cos - other.vx * sin

            # Collision elastic equations
            vx1, vx2 = ((self.mass - other.mass) * vx1 + 2 * other.mass * vx2) / (self.mass + other.mass), \
                       ((other.mass - self.mass) * vx2 + 2 * self.mass * vx1) / (self.mass + other.mass)

            # Rotate velocities back
            self.vx = vx1 * cos - vy1 * sin
            self.vy = vy1 * cos + vx1 * sin
            other.vx = vx2 * cos - vy2 * sin
            other.vy = vy2 * cos + vx2 * sin

            # Move balls apart to prevent sticking
            overlap = 0.5 * (self.radius + other.radius - distance + 1)
            self.x += overlap * cos
            self.y += overlap * sin
            other.x -= overlap * cos
            other.y -= overlap * sin

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)