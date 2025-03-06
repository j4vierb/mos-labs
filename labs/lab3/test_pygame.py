import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Test")

# Set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the circle properties
circle_radius = 25
circle_pos = [50, height // 2]
circle_speed = 3

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle position
    circle_pos[0] += circle_speed
    if circle_pos[0] > width + circle_radius:
        circle_pos[0] = -circle_radius

    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw the circle
    pygame.draw.circle(screen, RED, (int(circle_pos[0]), int(circle_pos[1])), circle_radius)
    
    # Update the display
    pygame.display.flip()
    
    # Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()

