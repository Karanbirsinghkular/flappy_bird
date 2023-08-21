import pygame

class Bird():
    def __init__(self, posx, length, breadth, w, h, gravity, anggrav, alive_color, dead_color):
        self.posx = posx
        self.posy = h / 2
        self.vely = 0
        self.accy = 0
        self.breadth = breadth
        self.length = length
        self.w = w
        self.h = h
        self.alive = True
        self.gravity = gravity
        self.anggrav = anggrav
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.im = pygame.image.load(r"D:\flap30.png").convert()
        self.im.set_colorkey((0, 0, 0, 0))
        self.angle = 0
        self.angvel =0

    def checkinbounds(self):
        return  self.posy  < self.h


    def applyForce(self,force):
        self.accy += force

    def applyGravity(self):
        self.applyForce(self.gravity)
        self.angvel += self.anggrav

    def jump(self, forcey, angvel):
        if self.alive:
            self.applyForce(forcey)
            self.vely = 0
            self.angvel = angvel
            self.angvel = min(angvel, max(self.angvel, - 5 * self.anggrav))

    def update(self,dt):
        self.applyGravity()

        self.vely += self.accy * dt
        self.posy += self.vely * dt + self.accy * dt * dt

        self.angle += self.angvel
        self.angle = min(20, max(self.angle, -15))

        self.accy = 0

    def show(self,screen):
        # self.im = pygame.transform.rotate(self.im, self.angle)
        # screen.blit(self.im, (self.posx, self.posy, self.breadth, self.length))
        self.blitRotateCenter(screen, self.im, self.posx, self.angle)

    def setAlive(self, state):
        if self.alive:
            self.alive = state
        else:
            return

    def getAlive(self):
        return self.alive

    def blitRotateCenter(self, screen, image, topleft, angle):

        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc

        screen.blit(rot_sprite, (self.posx, self.posy, self.breadth, self.length))