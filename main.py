import pygame
import random
from ball import Ball  # Import the Ball class

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncy Balls Simulation")

# Colors
BLACK = (0, 0, 0)

# Create balls
balls = [Ball(random.randint(50, width-50), random.randint(50, height-50), random.randint(10, 30)) for _ in range(10)]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for ball in balls:
        ball.move()
        ball.bounce_walls(width, height)
        for other in balls:
            if ball != other:
                ball.collide(other)
        ball.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()