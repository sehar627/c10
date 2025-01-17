import pygame

# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = 600
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Basic Pygame Window")

# Game loop
running = True
while running:
    # Fill the screen with a white background
    display.fill((255, 255, 255))

    # Update display
    pygame.display.flip()
