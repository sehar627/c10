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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detect window close
            running = False

    # Fill the screen with a white background
    display.fill((255, 255, 255))
    
    #Create the snake

    # Update display
    pygame.display.flip()

pygame.quit()
