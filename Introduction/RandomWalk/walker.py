import random

import pygame


def get_new_loc(pos):
    pos_li = list(pos)
    pos_li[0] += random.choice([-1, 1])
    pos_li[1] += random.choice([-1, 1])
    return tuple(pos_li)

if __name__ == "__main__":
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    pygame.init()
    pygame.display.set_caption("Random Walker")
    screen = pygame.display.set_mode((600, 600), 0, 32)
    screen.fill(WHITE)

    last_pos = (300, 300)
    mouse_position = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        mouse_position = get_new_loc(last_pos)
        pygame.draw.line(screen, BLACK, last_pos, mouse_position, 3)
        last_pos = mouse_position
        pygame.display.update()
