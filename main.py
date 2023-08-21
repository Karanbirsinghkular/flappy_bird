import time

import pygame, sys, bird, pipe, game_manager
from PIL import Image

w = 780
h = 480

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("FLAPPY BIRD")
my_font = pygame.font.SysFont('Comic Sans MS', 30)


red = (255, 0, 0, 0)
blue = (0, 0, 255, 0)
green = (0, 255, 255, 0)
gravity = 0.015          # 0.015
pipe_velx = -0.85        # -0.85
pipe_dist_ll = 200       # 200
pipe_dist_ul = 300       # 300
dt = 1                   # 1
acc = -1.4               # -1.4
lower_space_limit = 130  # 130
upper_space_limit = 150  # 150
breadth_ll = 50          # 50
breadth_ul = 70          # 70
anglejump = 1            # 1
anggrav = -0.01          # -0.01

start = False

flap = bird.Bird(10, 30, 30, w, h, gravity, anggrav, blue, red)
game = game_manager.Game_manager(flap, pipe_velx, pipe_dist_ll, pipe_dist_ul, green, w, h, lower_space_limit, upper_space_limit, breadth_ll, breadth_ul)
back = pygame.image.load(r"D:\background.png").convert()
back = pygame.transform.scale(back, (w, h))
while True:
    screen.fill((0, 0, 0, 0))
    screen.blit(back, (0, 0, w, h))
    if start:
        game.update(dt)
        time.sleep(0.003)
    game.show(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            start = True
            game.birdjump(acc, anglejump)
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = False
            flap = bird.Bird(10, 30, 30, w, h, gravity, anggrav, blue, red)
            game = game_manager.Game_manager(flap, pipe_velx, pipe_dist_ll, pipe_dist_ul, green, w, h,
                                             lower_space_limit, upper_space_limit, breadth_ll, breadth_ul)
            game.bird.setAlive(True)
    text_surface = my_font.render(str(game.score), False, (255, 255, 255))
    screen.blit(text_surface, (w / 2 - 25, 50))


    pygame.display.update()