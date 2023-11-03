import pygame
import sys
import os

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл {name} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if not colorkey:
        image = image.convert_alpha()
    elif colorkey == -1:
        image.set_colorkey(image.get_at((0, 0)))
    else:
        image.set_colorkey(colorkey)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    image = load_image('data/button.png')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        screen.blit(image, (250, 250))
        pygame.display.flip()
    pygame.quit()
