import pygame

# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = 600
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Moving Rectangle")

# Rectangle properties
rect_x = 250  # Initial x-coordinate
rect_y = 250  # Initial y-coordinate


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detect window close
            running = False

    # Move the rectangle
    rect_x += 2
    rect_y += 2

    # Check for collision with window boundaries
    
    # Fill the screen with a white background
    display.fill((255, 255, 255))

    # Draw the rectangle
    pygame.draw.rect(display, (0, 0, 0), (rect_x, rect_y, 20,20))

    # Update display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
