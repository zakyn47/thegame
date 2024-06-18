import pygame
from settings import *


def show_start_screen(screen):
    start_button = Button(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2, 100, 50, 'Start')
    quit_button = Button(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 60, 100, 50, 'Quit')

    running = True
    while running:
        screen.fill("black")
        start_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start_button.is_clicked(pos):
                    running = False
                elif quit_button.is_clicked(pos):
                    pygame.quit()


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, "white")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)




class Button:
    def __init__(self, x, y, width, height, text=None, color=(73, 73, 73), hover_color=(189, 189, 189), font_size=30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font_size = font_size

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text:
            font = pygame.font.Font(None, self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_clicked(self, mouse_position):
        if self.x < mouse_position[0] < self.x + self.width:
            if self.y < mouse_position[1] < self.y + self.height:
                return True
        return False