import pygame

class Pipe():
    def __init__(self, posx, l1, breadth, space, w, h, color):
        self.posx = posx
        self.l1 = l1
        self.space = space
        self.l2 = h - l1 - space
        self.breadth = breadth
        self.w = w
        self.h = h
        self.color = color
        self.pipe_body = pygame.image.load(r"D:\pipe_body.png").convert()
        self.pipe_end = pygame.image.load(r"D:\pipe_end.png").convert()

    def checkinbounds(self):
        return 0 <= self.posx + self.breadth

    def update(self, velx, dt):
        self.posx += velx * dt

    def show(self, screen):
        try:
            im = pygame.transform.scale(self.pipe_body, (self.breadth, self.l1 - 50))
        except:
            pass
        else:
            screen.blit(im, (self.posx, 0, self.breadth, self.l1 - 50))
        im = pygame.transform.scale(self.pipe_end, (self.breadth, 50))
        screen.blit(im, (self.posx, self.l1 - 50, self.breadth, 50))
        #pygame.draw.rect(screen, self.color, pygame.Rect(self.posx, 0, self.breadth, self.l1))
        #pygame.draw.rect(screen, self.color, pygame.Rect(self.posx, self.l1 + self.space,self.breadth, self.l2))
        im2 = pygame.transform.scale(self.pipe_end, (self.breadth, 50))
        screen.blit(im2, (self.posx, self.l1 + self.space, self.breadth, 50))
        try :
            im = pygame.transform.scale(self.pipe_body, (self.breadth, self.l2 - 50))
        except:
            pass
        else:
            screen.blit(im, (self.posx, self.l1 + self.space + 50, self.breadth, self.l2 - 50))

    def checkinpipe(self, bird):
        return ((self.posx < bird.posx + bird.breadth) and (bird.posx < self.posx + self.breadth)) and \
            not ((self.l1 < bird.posy) and(bird.posy + bird.length < self.l1 + self.space))