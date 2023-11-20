"""
installation pygame doesn't work when compiler is anaconda..? Try python 3.11
"""
import pygame

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

window_width = screen_width // 2
window_height = screen_height // 2

window_surface = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Green Fuckin' Square")

square_size = 50
square_x, square_y = 0, 0

green = (0, 255, 0)

max_move_pixels = 2
# TODO Fix windows size to run it in fullscreen mode
# TODO Fix square movements
phases = [
    ["right", window_width - square_size, 0],    # Move to the right upper corner
    ["down", window_width - square_size, window_height - square_size],  # Move to the left lower corner
    ["left", 0, window_height - square_size],    # Move to the upper left corner
    ["up", 0, 0]                                # Move back to the left upper corner
]

current_phase = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Resize the window
            window_width = event.w
            window_height = event.h
            window_surface = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

    phase_direction, target_x, target_y = phases[current_phase]

    move_x = max_move_pixels if target_x > square_x else -max_move_pixels
    move_y = max_move_pixels if target_y > square_y else -max_move_pixels

    square_x += move_x
    square_y += move_y

    if (move_x > 0 and square_x >= target_x) or (move_x < 0 and square_x <= target_x):
        square_x = target_x
    if (move_y > 0 and square_y >= target_y) or (move_y < 0 and square_y <= target_y):
        square_y = target_y

        current_phase += 1
        current_phase %= len(phases)  # Wrap around if reaching the end of the phases

    window_surface.fill((255, 255, 255))

    pygame.draw.rect(window_surface, green, (square_x, square_y, square_size, square_size))

    pygame.display.flip()

    pygame.time.delay(50)


pygame.quit()