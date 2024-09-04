import pygame
from typing import List, Tuple

def draw_moving_square(window_surface, window_width: int, window_height: int, square_size: int = 50, max_move_pixels: int = 2) -> None:
    """
    Отрисовывает движущийся зеленый квадрат по экрану.

    Args:
        window_surface: Поверхность окна Pygame.
        window_width (int): Ширина окна.
        window_height (int): Высота окна.
        square_size (int): Размер квадрата.
        max_move_pixels (int): Максимальное количество пикселей для движения за шаг.
    """
    green = (0, 255, 0)  
    square_x, square_y = 0, 0  

    phases: List[Tuple[str, bool]] = [
        ("right", True),
        ("down", False),
        ("left", True),
        ("up", False)
    ]
    current_phase = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        phase_direction, is_horizontal = phases[current_phase]

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

        current_phase %= len(phases)

        window_surface.fill((255, 255, 255))

        pygame.draw.rect(window_surface, green, (square_x, square_y, square_size, square_size))

        pygame.display.flip()

        pygame.time.delay(5)

    pygame.quit()

pygame.init()

window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Green Square")
window_width, window_height = pygame.display.get_surface().get_size()

draw_moving_square(window_surface, window_width, window_height)