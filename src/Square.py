import pygame

# Initialize Pygame
pygame.init()

# Create the window surface
window_surface = pygame.display.set_mode((800, 600))  # Set your desired window dimensions
pygame.display.set_caption("Green Square")

# Set the initial position of the square
square_size = 50
square_x, square_y = 0, 0

# Set the green color (R, G, B)
green = (0, 255, 0)

# Set the maximum number of pixels to move in each frame
max_move_pixels = 2

# Set the movement phases
phases = [
    ["right", True],   # Move to the right window border
    ["down", False],   # Move to the bottom window border
    ["left", True],    # Move to the left window border
    ["up", False]      # Move to the top window border
]

# Set the initial phase index
current_phase = 0

# Get the window dimensions
window_width, window_height = pygame.display.get_surface().get_size()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current phase details
    phase_direction, is_horizontal = phases[current_phase]

    # Update the square position based on the current phase
    if phase_direction == "right":
        square_x += max_move_pixels
        if square_x >= window_width - square_size:
            square_x = window_width - square_size
            current_phase += 1
    elif phase_direction == "down":
        square_y += max_move_pixels
        if square_y >= window_height - square_size:
            square_y = window_height - square_size
            current_phase += 1
    elif phase_direction == "left":
        square_x -= max_move_pixels
        if square_x <= 0:
            square_x = 0
            current_phase += 1
    elif phase_direction == "up":
        square_y -= max_move_pixels
        if square_y <= 0:
            square_y = 0
            current_phase += 1

    # Wrap around the phases if reaching the end
    current_phase %= len(phases)

    # Fill the window with a white background
    window_surface.fill((255, 255, 255))

    # Draw the green square
    pygame.draw.rect(window_surface, green, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()
    # Delay for a short time
    pygame.time.delay(5)

# Quit Pygame
pygame.quit()