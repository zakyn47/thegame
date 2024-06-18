import pygame
from settings import *
from sprites import *
from start_screen import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Thegame")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    running = True
    show_start_screen(screen)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill("black")
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()