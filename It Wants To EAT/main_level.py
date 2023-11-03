from load_image import load_image
import pygame
import random
import time


class Hero(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = hero_image
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(250, 400))
        self.is_jump, self.is_jump_dir = False, False
        self.jump_count, self.right, self.left = 10, True, False


    def update(self, *args):
        if pygame.sprite.collide_mask(self, rancid_pelmeni):
            collision = True
        if not self.is_jump:
            time.sleep(0.015)
            self.rect.y += 5
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] and 0 < self.rect.y < 500:
                self.is_jump = True
        else:
            keys = pygame.key.get_pressed()
            if self.jump_count >= -10 and keys[pygame.K_d]:
                self.rect.y -= self.jump_count
                self.jump_count -= 1
                self.rect.x += 3
                time.sleep(0.015)
            elif self.jump_count >= -10 and keys[pygame.K_a]:
                self.rect.y -= self.jump_count
                self.jump_count -= 1
                self.rect.x -= 3
                time.sleep(0.015)
            elif self.jump_count >= -10 and keys[pygame.K_w]:
                self.rect.y -= self.jump_count
                self.jump_count -= 1
                time.sleep(0.02)
            else:
                self.is_jump, self.jump_count = False, 15 + 5
                self.rect.y += self.jump_count

class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = enemy_image
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(center=(250, 400))
        self.mask = pygame.mask.from_surface(self.image)
        self.you_win = you_win_image
        self.is_collided = False

    def update(self, *args):
        global running
        self.rect.x = hero.rect.x - 100
        self.rect.y = 250
        if pygame.sprite.collide_mask(self, hero):
            self.is_collided = True
            if enemy.is_collided:
                screen.blit(gs.gameover_image, (0, 0))
                if gs.rect.x < 0:
                    gs.rect.x += speed
                running = False
        if len(all_sprites) < 30:
            screen.blit(self.you_win, (0, 0))
            if gs.rect.x < 0:
                gs.rect.x += speed



class Pelmeni(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pelmen_image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, width - 50)
        self.rect.y = random.randint(-10000, height)
        self.color = pygame.Color('#72aee6')
        self.font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 12)
        self.text = ''
        self.symbol = self.font.render(self.text, True, self.color)
        self.is_collided = False
        self.direction = 0
        self.lst = []

    def update(self, *args):
        if self.rect.x >= 450:
            self.direction = 1
        if self.rect.x <= 0:
            self.direction = 2
        if self.direction % 2 == 0:
            self.rect.x += 3
        elif self.direction % 2 != 0:
            self.rect.x -= 3

        if pygame.sprite.collide_mask(self, hero):
            self.is_collided = True
            self.kill()

    def collected(self):
        if self.is_collided:
            self.text = f'{len(all_sprites)} I 40'
            self.symbol = self.font.render(self.text, True, self.color)
            screen.blit(self.symbol, (385, 461))


class RancidPelmeni(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = rancid_pelmen
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, width - 50)
        self.rect.y = random.randint(-10000, height)
        self.color = pygame.Color('#FF0000')
        self.font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 12)
        self.text = ''
        self.symbol = self.font.render(self.text, True, self.color)
        self.is_collided = False
        self.direction = 0

    def update(self, *args):
        if self.rect.x >= 450:
            self.direction = 1
        if self.rect.x <= 0:
            self.direction = 2
        if self.direction % 2 == 0:
            self.rect.x += 1
        elif self.direction % 2 != 0:
            self.rect.x -= 1

        if pygame.sprite.collide_mask(self, hero):
            self.is_collided = True
            self.image = pygame.transform.scale(self.image, (0, 0))



class BoostPelmeni(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = boost_pelmen
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, width - 50)
        self.rect.y = random.randint(-10000, height)
        self.color = pygame.Color('#72aee6')
        self.font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 12)
        self.text = ''
        self.symbol = self.font.render(self.text, True, self.color)
        self.is_collided = False
        self.direction = 0

    def update(self, *args):
        if self.rect.x >= 450:
            self.direction = 1
        if self.rect.x <= 0:
            self.direction = 2
        if self.direction % 2 == 0:
            self.rect.x += 10
        elif self.direction % 2 != 0:
            self.rect.x -= 10

        if pygame.sprite.collide_mask(self, hero):
            self.is_collided = True
            self.image = pygame.transform.scale(self.image, (0, 0))


class InfoBox:
    def __init__(self, text):
        self.color = pygame.Color('#72aee6')
        self.font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 12)
        self.text = text
        self.symbol = self.font.render(self.text, True, self.color)

    def show_data(self):
        global running
        global time_left
        if time_left >= 0:
            time_left -= 1
            time.sleep(1)
            self.text = f'{int(time_left)} sec'
        else:
            running = False
        self.symbol = self.font.render(self.text, True, self.color)
        screen.blit(self.symbol, (200, 461))

class GameOverSprite(pygame.sprite.Sprite):
    def __init__(self, x, image):
        pygame.sprite.Sprite.__init__(self)
        self.gameover_image = image
        self.rect = self.gameover_image.get_rect(center=(x, 250))

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.y += self.dy - 50

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)

def open_ent_window():
    from enterance_window import EnteranceWindow
    return EnteranceWindow


pygame.init()
speed = 6
FPS = 30
time_left = 60
text = ''
num = 0
clock = pygame.time.Clock()
pelmen_image = pygame.image.load('data/pelmen.png')
rancid_pelmen = pygame.image.load('data/rancid_pelmen.png')
hero_image = pygame.image.load('data/shlepa_in_the_basket.png')
enemy_image = pygame.image.load('data/enemy (3) (1).png')
info_bar_image = pygame.image.load('data/info_bar_2.png')
boost_pelmen = pygame.image.load('data/boost_pelmen.png')
background_image = pygame.image.load('data/clouds.png')
ending_image = pygame.image.load('data/dark_souls.png')
you_win_image = pygame.image.load('data/you_win.jpg')
ending_image = pygame.transform.scale(ending_image, (500, 500))
background_image = pygame.transform.scale(background_image, (500, 500))
you_win_image = pygame.transform.scale(you_win_image, (500, 500))
pelmen_image_2 = pygame.transform.scale(pelmen_image, (30, 30))
all_sprites = pygame.sprite.Group()
hero = pygame.sprite.Group
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('It Wants to EAT')
camera = Camera()
hero = Hero(all_sprites)
enemy = Enemy(all_sprites)
ib = InfoBox('')
gs = GameOverSprite(150, ending_image)
bg_x = 0
for _ in range(30):
    pelmeni = Pelmeni(all_sprites)
for _ in range(5):
    rancid_pelmeni = RancidPelmeni(all_sprites)
for _ in range(5):
    boost_pelmeni = BoostPelmeni(all_sprites)
pelmeni = Pelmeni(all_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        camera.update(hero)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.update(event)
    if not enemy.is_collided:
        screen.blit(background_image, (0, bg_x))
        screen.blit(background_image, (0, bg_x - 500))
        bg_x += 2
        if bg_x == 500:
            bg_x = 0
        all_sprites.update()
        all_sprites.draw(screen)
        screen.blit(info_bar_image, (0, 449))
        screen.blit(pelmen_image_2, (335, 457))
        ib.show_data()
        pelmeni.collected()
        pygame.display.flip()
time.sleep(3)
open_ent_window()