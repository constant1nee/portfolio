import pygame
import time
from load_image import load_image

pygame.init()
pygame.display.set_caption('It Wants To EAT')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
passive_sign_in_btn = load_image('pixil-frame-0 (4).png')
active_sign_in_btn = load_image('pixil-frame-0 (5).png')
passive_sign_up_btn = load_image('pixil-frame-0 (12).png')
active_sign_up_btn = load_image('pixil-frame-0 (10).png')
passive_settings_btn = load_image('pixil-frame-0 (14).png')
active_settings_btn= load_image('pixil-frame-0 (15).png')

class EnteranceWindow:
    def __init__(self, screen):
        self.screen = screen

    def background_image(self):
        image = pygame.image.load('data\shlepa.png').convert_alpha()
        rect = image.get_rect()
        self.screen.blit(image, rect)

    def draw_title(self):
        font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 28)
        title = font.render('It Wants To Eat', True, '#72aee6')
        pos = title.get_rect(center=(250, 100))
        self.screen.blit(title, pos)
        pygame.display.update()


class Button(pygame.sprite.Sprite):
    def __init__(self, group, x, btn_passive, btn_active, on_click):
        super().__init__(group)
        self.btn_passive, self.btn_active = btn_passive, btn_active
        self.image = btn_passive
        self.on_click = on_click
        self.rect = self.image.get_rect(center=(250, 200 + x))

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(args[0].pos):
                self.image = self.btn_active
            else:
                self.image = self.btn_passive
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
             self.on_click()

screen.fill((20, 20, 20))
ew = EnteranceWindow(screen)
ew.draw_title()
all_sprites = pygame.sprite.Group()
running = True

def open_sign_in():
    from sign_in_window import SignInWindow
    return SignInWindow

def open_sign_up():
    from sign_up_window import SignUpWindow
    return SignUpWindow

def open_nothing():
    pass

button = Button(all_sprites, 0, passive_sign_in_btn, active_sign_in_btn, open_sign_in)
button_2 = Button(all_sprites, 75, passive_sign_up_btn, active_sign_up_btn, open_sign_up)
button_3 = Button(all_sprites, 150, passive_settings_btn, active_settings_btn, open_nothing)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
time.sleep(1)
pygame.quit()
time.sleep(3)